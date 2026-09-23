`this README will be updated regularly to fit new update content!`

# Judie bot Project Repository

|  General Info  | |
| ---|---|
| Working Title | `Judie Bot` |
| Developer | `Eisritter` |
| Target Platform(s) | `Discord` |
| Start Date | July 2021 |
| Current Version | 3.0.2 |

### Abstract

In this project, I will work on making a discord bot for the Caribdis Games community. Said bot will contain the following list of features, which may be expanded to the developer's and community's wishes:
- OiaLt gf game
- Eternum gf game
- OiaLt & Eternum nsfw command
- Miscellaneous greeting commands

## Repository Usage Guides

```
root/
    ├── README.md           // This should reflect the project accurately,
    │                       //  so always contains information about the bot 
    │                       //  and its functions. 
    ├── CHANGELOG           // Logs all the update notes for the latest 
    │                       //  general update and latest major update!
    └── code/               // Project code and attachements are in here!
    └── visual/             // Any graphics (icons, emotes) used for Judie's 
    │                       //  Application profile are included here.
    └── instructions.md     // Instructions on how to use this repository to 
    │                       //  import Judie to your servers + modding!
```

## Changelog Judie V3.0.0

*Deployed on Aug. 2nd, 2026*
Big functional update, bringing required support for slash commands + persistent cooldowns + mod-exclusive commands

### Changes:
- Another huge chunk of __behind-the-scenes refactoring__ which has finally reached the last files of the project, so that major rew*rk is now behind me! I'm now working on making test scenarios to make at least the database changes more robust to change, but that was rudely interrupted by the need to switch to slash commands.
- the `-gf` and `-update` commands, which were easter egg remnants of Judie's earliest days have been __retired__, as they weren't worth updating to slash 🫡 
- `/timers` are __safe to use__ again after a hotfix earlier this month
- Added the **moderator-exclusive** commands to: 
> - **gift characters** (to make up for individual, accidental losses that seem to have cropped up over time. Characters will not be granted without explicit proof they have been robbed in some way), 
> - **Port progress** from one account to another, for the case you should want to switch to a different main account for whatever reason. (community-requested command)
> - **Reset cooldowns** again to make up for individual breaks, or to reward the whole server.
- Added the ability to __view others' progress on collections__! Just feed the discord ID as an option to collections commands!
- Switched the __cooldown__ mapping to use a similar approach to the one used for Nancy a while ago, meaning cooldowns are now *persistent to outages*. (Cooldowns can still be reset as described above as apologies for unexpected outages or bigger updates, don't worry :)

And that's about it, thank you for your patience, and I wish you a happy time pulling characters again!

## Self-hosting Judie & Modding:

The main instance of Judie in Caribdis' server is deliberately not invitable to your private servers, for missing scalability and flexibility. You *can* however download this repository and make your own clone of Judie to invite yourself! I've made a full guide to do so [here](instructions.md)!
> This guide also explains how you can modify certain features of the bot for your deployment, to make it more fun and personal :) 

## Judie's OiaLt gf game description:

Pull a partner from the Once in a Lifetime universe once every 23h. Different characters can be collected or impact your collections:

*Requires registration to track progress in a protected database that stores only your discord user ID as information!*

### Harem:

Collect Judie, Lauren, Messy Hair Lauren, Carla, Iris, Jasmine, Aiko and Rebecca for a total of 8 harem members!

Beware! For Orochi will likely buy off a harem member, preferring any version of Lauren, unless you're protected by the Funtime Clan Leader!

Check your progress with -harem !

### Stabby Clan:

Collect Father Mitchell, Mike the Yakuza, Mike the Exterminator, Mike the Policeman, Mike the Hitman, and Anastasia for a total of 6 stabby clan members!

Beware! For Astaroth will likely kill off a clan member, preferring Father Mitchell, unless you're protected by the Once in a Lifetime MC!

Check your progress with -stabbyclan !

### The Boys:

Collect MC, Tom, Fit Jack, Hiromi, Asmodeus, and Oliver for a total of 6 members of the boys!

Beware! For Azazel will likely kill off one of the boys, preferring the MC, unless you're protected by Aiko!

Check your progress with -theboys !

### Potential LI's:

Collect Ava, the Shop Girl, the Train Conductor, Fit Jack's Groupie, the Stone Elephant, and Lilith for a total of 6 potential LI's!

Beware! For Monster Lilith will likely mutate a potential LI, preferring Lilith, unless 93 gets to chase her away before hand!

Check your progress with -potentialLis !

### More Info:

The protection and membership in a collection are independent from another! Even if Orochi buys off Aiko, she will still protect the boys!
Delete your data stored by Judie any time with -deleteacc!

## Judie's Eternum gf game description:

In a much similar fashion to the Eternum game, Judie offers a collectible game for Eternum characters, enhanced to a higher level of visual feedback - character cards are organized in a mobile-friendly aspect ratio, and feature colors and emotes to showcase the results of the pull, beyond the classic character card features.

As with Oialt, the goal is to collect the following characters:

### Harem:

Collect Alex, Annie, Dalia, Luna, Nancy, Nova and Penny (7 characters).

Beware! For Thanatos is out for blood, and will collect the souls of any unfortunate LI he comes across, especially Alex and Nova. Only Calypso is powerful enough to stand up to him!

Check your progress with '-eharem' !

### The Homies:

Collect Chang, Chop-Chop, Victor, Jerry, Micaela, Noah, Orion and Raul (8 characters).

Beware! A vicious troll has been spotted smashing in ill-fortuned heads. Keep your Jerries safe! If only Dalia was around to save him!

Check your progress with '-homies' !

### Side Girls:

Collect Blue Fox Maiden, Calypso, Eva, Idriel, Maat, Red Fox Maiden and Wenlin (7 characters).

Beware! Axel was spotted lurking around, he might have his way with any piece of skin he can get his hand on! Make sure Orion is around to punch his face in if he tries!

Check your progress with '-sidegirls' !

### Creatures:

Collect Carolyn, Igor, Kermit, Maurice (cat), Maurice (goat), Maurice (toucan) and Pancho (6 characters).

Beware! A vicious Golem was summoned to stamp any poor creature it comes across. Make sure to summon Pyramid Head to protect your animal friends.

Check your progress with '-creatures'

## Other commands:

### Good morning and Good night:

-gm

-gn

### Nsfw command:

use '-nsfw' (In a channel marked as such!) to get a random lewd render from the Once in a Lifetime or Eternum games!

You can add filters by adding one (!) name after the command issued, e.g. -nsfw Annie!

Currently supported filters are:

- OiaLt/Once in a Lifetime

- Eternum

- Judie; Lauren; Carla; Iris; Jasmine; Aiko; Rebecca

- Alex/Alexandra; Annie; Calypso; Dalia; Eva; FoxMaidens; Luna; Maat; Nancy; Nova; Orion; Penny; Wenlin; 

(Filter typing is case insensitive, you could write pENeLOpE and it'll give you a juicy penny image)
