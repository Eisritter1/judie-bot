# DISCORD LIBRARIES
import discord
from discord import app_commands
from discord.ext import commands
# EXTERNAL LIBRARIES
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime
import os, pickle, pytz

# time = time in seconds until timer ends -> will be used for cooldowns!
class TimeObject:
    """
    Struct for more intuitive use of time. Takes a certain interval in seconds as input.
    -----------------------------------------------------
    Parameters:
        - hours : int
        - minutes : int
        - seconds : int
    """
    def __init__(self, time):
        self.hours = int(time // 3600)
        self.minutes = int((time % 3600) // 60)
        self.seconds = int((time % 3600) % 60)

    def get_time(self) -> str:
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def is_empty(self) -> bool:
        return self.hours == 0 and self.minutes == 0 and self.seconds == 0

class TimerRecord:
    def __init__(self, _cooldown: int):
        self.timestamp = datetime.now(tz=pytz.UTC)
        self.cooldown = _cooldown

    def active(self) -> bool:
        return (datetime.now(tz=pytz.UTC) - self.timestamp).total_seconds() < self.cooldown

    def get_retry_after(self) -> TimeObject:
        elapsed = (datetime.now(tz=pytz.UTC) - self.timestamp).total_seconds()
        # return a time object worth either cooldown - elapsed time (a.k.a. time left until cooldown expires), 
        # or 0 if the cooldown is expired (elapsed time > cooldown).
        return TimeObject(max(0, float(self.cooldown) - elapsed))

def check_cooldown():
    """
    Checks whether a registered user is subject to a timer or not.
    """
    async def predicate(interaction: discord.Interaction):
        return await Timekeeper.trigger_timer(interaction.command, interaction.user)
    return app_commands.check(predicate)

load_dotenv()
GUILD = discord.Object(id=os.getenv("GUILD"))

class Timekeeper(commands.Cog):
    dict_path = "./storage/"
    file_prefix = "cooldowns_"
    cooldown = 0

    async def init(client: discord.ext.commands.Bot):
        Timekeeper.cooldown = client.config.cooldown

    async def trigger_timer(cmd: app_commands.Command, user: discord.User):
        # command name counts as identifier since can't be duplicated.
        cmd_id = cmd.name

        # load dict
        cmd_dict = await Timekeeper.load_dict(cmd_id)
        # create a dummy entry if no existing dict for the command.
        if cmd_dict is None:
            cmd_dict = {user.id: TimerRecord(0)}

        # exit early if still bound by timer.
        cooldown: TimerRecord = cmd_dict[user.id]
        if cooldown.active():
            raise CommandOnCooldownError(user.display_name, cmd_id, cooldown.get_retry_after())

        # replace the timer record & save to disk before exiting successfully
        cmd_dict[user.id] = TimerRecord(Timekeeper.cooldown)
        await Timekeeper.save_dict(cmd_id, cmd_dict)
        return True

    async def read_timer(cmd: app_commands.Command, user: discord.User) -> TimeObject:
        cmd_id = cmd.name

        # load dict
        cmd_dict = await Timekeeper.load_dict(cmd_id)
        # is not in cooldown if no records
        if cmd_dict is None:
            return TimeObject(0)

        # is not in cooldown if user not known to records
        if user.id not in cmd_dict:
            return TimeObject(0)

        entry: TimerRecord = cmd_dict[user.id]
        return entry.get_retry_after()

    async def amend_timer(cmd: app_commands.Command, user: discord.User, val: int):
        cmd_id = cmd.name

        # load dict
        cmd_dict = await Timekeeper.load_dict(cmd_id)
        # is not in cooldown if no records
        if cmd_dict is None:
            # throw custom error here eventually :)
            return

        # is not in cooldown if user not known to records
        if user.id not in cmd_dict:
            return

        entry: TimerRecord = cmd_dict[user.id]
        entry.cooldown = val
        await Timekeeper.save_dict(cmd_id, cmd_dict)

    async def reset_timer(cmd: app_commands.Command, user: discord.User) -> bool:
        cmd_id = cmd.name

        # load dict
        cmd_dict = await Timekeeper.load_dict(cmd_id)
        # is not in cooldown if no records
        if cmd_dict is None:
            # throw custom error here eventually :)
            return

        # is not in cooldown if user not known to records
        if user.id not in cmd_dict:
            return False

        entry: TimerRecord = cmd_dict[user.id]
        entry.timestamp = datetime.now(tz=pytz.UTC)
        await Timekeeper.save_dict(cmd_id, cmd_dict)
        return True

    async def reset_all_timers(cmd: app_commands.Command):
        cmd_id = cmd.name

        # load dict
        cmd_dict = await Timekeeper.load_dict(cmd_id)
        # is not in cooldown if no records
        if cmd_dict is None:
            # throw custom error here eventually :)
            return

        # one timestamp so all timers are reset to the same value.
        timestamp = datetime.now(tz=pytz.UTC)

        # iterate over all records to set all from the same time. 
        # timestamps set to expire exactly at value assignment
        for record in cmd_dict.values():
            record.timestamp = timestamp - datetime.timedelta(seconds=record.cooldown)

        await Timekeeper.save_dict(cmd_id, cmd_dict)

    async def save_dict(cmd_id: str, cooldown_dict: dict):
        _path = os.path.join(Timekeeper.dict_path, f"{Timekeeper.file_prefix}{cmd_id}.pkl")
        os.makedirs(Timekeeper.dict_path, exist_ok=True)

        with open(_path, "wb") as f:
            pickle.dump(cooldown_dict, f)
        return cooldown_dict

    async def load_dict(cmd_id: str) -> dict:
        _path = os.path.join(Timekeeper.dict_path, f"{Timekeeper.file_prefix}{cmd_id}.pkl")
        if(os.path.isfile(_path)):
            with open(_path, 'rb') as f:
                return pickle.load(f)

        # if no dict saved, return a null value
        return 


class CommandOnCooldownError(app_commands.AppCommandError):
    def __init__(self, user_display_name: str, command_name: str, retry_after: TimeObject):
        self.user_display_name = user_display_name
        self.command_name = command_name
        self.retry_after = retry_after
        super().__init__(f"User {user_display_name} is still on cooldown for "\
            f"the command {command_name}!")
