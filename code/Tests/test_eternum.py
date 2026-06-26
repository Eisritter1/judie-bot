import pytest, sqlite3, os, sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from Eternum import Eternum
from Utilities import Collections, Effects
from CharacterCard import CharacterCard, Villain

# Pytest fixture setup
test_id = 0

class FakeClient:
    db_path = "Tests/test.sqlite"

    def __init__(self):
        self.config={
            "deployment": "TEST"
        }
        self.db_path = FakeClient.db_path
        self.accountManager = None
        self.CogsToActivate = []

def createAndUpdateDatabase():
    """
    Defines the structure of the Judie Bot Database and updates the database's contents afterwards.
    """

    db = sqlite3.connect(FakeClient.db_path)
    cursor = db.cursor()

    print("Checking DB Integrity")

    #region users
    cursor.execute("""
            CREATE TABLE if NOT EXISTS users(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            discord_id TEXT
            )
            """)
    #endregion

#region Oialt
    #region Overview: oialt
    cursor.execute("""
            CREATE TABLE if NOT EXISTS oialt(
            user_id INTEGER,
            funtime INTEGER DEFAULT 0,
            mc INTEGER DEFAULT 0,
            aiko INTEGER DEFAULT 0,
            nine_three INTEGER DEFAULT 0,
            last_gf TEXT
            )
            """)
    #endregion

    #region Harem: oialt_harem
    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS oialt_harem(
                        user_id INTEGER,
                        judie TEXT DEFAULT NONE,
                        lauren TEXT DEFAULT NONE,
                        messy_hair_lauren TEXT DEFAULT NONE,
                        carla TEXT DEFAULT NONE,
                        iris TEXT DEFAULT NONE,
                        aiko TEXT DEFAULT NONE,
                        jasmine TEXT DEFAULT NONE,
                        rebecca TEXT DEFAULT NONE,
                        last_li TEXT
                        )
                        """)
    #endregion

    #region Stabby Clan: stabby_mikes
    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS stabby_mikes(
                        user_id INTEGER,
                        police TEXT DEFAULT NONE,
                        hitman TEXT DEFAULT NONE,
                        yakuza TEXT DEFAULT NONE,
                        priest TEXT DEFAULT NONE,
                        exterminator TEXT DEFAULT NONE,
                        anastasia TEXT DEFAULT NONE,
                        last_mike TEXT
                        )
                        """)
    #endregion

    #region The Boys: the_boys
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS the_boys(
                    user_id INTEGER,
                    mc TEXT DEFAULT NONE,
                    tom TEXT DEFAULT NONE,
                    oliver TEXT DEFAULT NONE,
                    fit_jack TEXT DEFAULT NONE,
                    asmodeus TEXT DEFAULT NONE,
                    hiromi TEXT DEFAULT NONE,
                    last_boi TEXT
                    )
                    """)
    #endregion

    #region Potential LI's: li_potential
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS li_potential(
                    user_id INTEGER,
                    ava TEXT DEFAULT NONE,
                    lilith TEXT DEFAULT NONE,
                    fit_jack_groupie TEXT DEFAULT NONE,
                    train_conductor TEXT DEFAULT NONE,
                    shop_girl TEXT DEFAULT NONE,
                    stone_elephant TEXT DEFAULT NONE,
                    last_potential_li TEXT
                    )
                    """)
    #endregion
#endregion

#region Eternum
    #region Overview: eternum
    cursor.execute("""
            CREATE TABLE if NOT EXISTS eternum(
            user_id INTEGER,
            orion INTEGER DEFAULT 0,
            calypso INTEGER DEFAULT 0,
            dalia INTEGER DEFAULT 0,
            pyramid_head INTEGER DEFAULT 0,
            last_gf TEXT
            )
            """)
    #endregion

    #region Harem: eternum_harem
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS eternum_harem(
                user_id INTEGER,
                alex TEXT DEFAULT NONE,
                annie TEXT DEFAULT NONE,
                dalia TEXT DEFAULT NONE,
                luna TEXT DEFAULT NONE,
                nancy TEXT DEFAULT NONE,
                nova TEXT DEFAULT NONE,
                penny TEXT DEFAULT NONE,
                last_girl TEXT,
                calypso TEXT DEFAULT NONE
                )
                """)
    #endregion

    #region The homies: homies
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS homies(
                user_id INTEGER,
                chang TEXT DEFAULT NONE,
                chopchop TEXT DEFAULT NONE,
                victor TEXT DEFAULT NONE,
                jerry TEXT DEFAULT NONE,
                micaela TEXT DEFAULT NONE,
                noah TEXT DEFAULT NONE,
                orion TEXT DEFAULT NONE,
                raul TEXT DEFAULT NONE,
                last_homie TEXT
                )
                """)
    #endregion

    #region Side Girls: side_girls
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS side_girls(
                user_id INTEGER,
                bluefoxmaiden TEXT DEFAULT NONE,
                lorelei TEXT DEFAULT NONE,
                eva TEXT DEFAULT NONE,
                idriel TEXT DEFAULT NONE,
                maat TEXT DEFAULT NONE,
                redfoxmaiden TEXT DEFAULT NONE,
                wenlin TEXT DEFAULT NONE,
                last_affair TEXT
                )
                """)
    #endregion

    #region Pets: creatures
    cursor.execute("""
                CREATE TABLE if NOT EXISTS creatures(
                user_id INTEGER,
                carolyn TEXT DEFAULT NONE,
                igor TEXT DEFAULT NONE,
                kermit TEXT DEFAULT NONE,
                mauricec TEXT DEFAULT NONE,
                mauriceg TEXT DEFAULT NONE,
                mauricet TEXT DEFAULT NONE,
                pancho TEXT DEFAULT NONE,
                last_creature TEXT
                )
                """)
    #endregion
#endregion

    #region DB update code
    # SQLite extra guides because I'll forget otherwise:
        # if EXISTS not supported in ALTER TABLE statements
        # UPDATE [table_name]
        # DROP COLUMN not supported as an ALTER TABLE function
    print("Performing Database Updates.")

    #region table oialt_harem to integer
    try:
        # create a temp table with the new type
        cursor.execute("""
            CREATE TABLE oharem_temp(
                user_id INTEGER,
                judie INTEGER DEFAULT 0,
                lauren INTEGER DEFAULT 0,
                messy_hair_lauren INTEGER DEFAULT 0,
                carla INTEGER DEFAULT 0,
                iris INTEGER DEFAULT 0,
                aiko INTEGER DEFAULT 0,
                jasmine INTEGER DEFAULT 0,
                rebecca INTEGER DEFAULT 0,
                last_li TEXT
            )
        """)

        # insert values derived from 'old' table
        cursor.execute("""
            INSERT INTO oharem_temp (user_id, judie, lauren, messy_hair_lauren, carla, iris, aiko, jasmine, rebecca, last_li)
            SELECT
                user_id,
                CASE WHEN COALESCE(judie, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(lauren, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(messy_hair_lauren, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(carla, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(iris, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(aiko, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(jasmine, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(rebecca, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                last_li
            FROM oialt_harem
        """)

        # drop old table
        cursor.execute("DROP TABLE oialt_harem")

        # rename 'new' table to oialt_harem
        cursor.execute("ALTER TABLE oharem_temp RENAME TO oialt_harem")

        db.commit()

    except Exception as e:
        print(f"[oialt_harem to int] {e}")
    #endregion

    #region table stabby_mikes to integer
    try:
        # create a temp table with the new type
        cursor.execute("""
            CREATE TABLE mikes_temp(
                user_id INTEGER,
                police INTEGER DEFAULT 0,
                hitman INTEGER DEFAULT 0,
                yakuza INTEGER DEFAULT 0,
                priest INTEGER DEFAULT 0,
                exterminator INTEGER DEFAULT 0,
                anastasia INTEGER DEFAULT 0,
                last_mike TEXT
            )
        """)

        # insert values derived from 'old' table
        cursor.execute("""
            INSERT INTO mikes_temp (user_id, police, hitman, yakuza, priest, exterminator, anastasia, last_mike)
            SELECT
                user_id,
                CASE WHEN COALESCE(police, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(hitman, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(yakuza, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(priest, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(exterminator, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(anastasia, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                last_mike
            FROM stabby_mikes
        """)

        # drop old table
        cursor.execute("DROP TABLE stabby_mikes")

        # rename 'new' table to oialt_harem
        cursor.execute("ALTER TABLE mikes_temp RENAME TO stabby_mikes")

        db.commit()

    except Exception as e:
        print(f"[stabby_mikes to int] {e}")
    #endregion

    #region table the_boys to integer
    try:
        # create a temp table with the new type
        cursor.execute("""
            CREATE TABLE boys_temp(
                user_id INTEGER,
                mc INTEGER DEFAULT 0,
                tom INTEGER DEFAULT 0,
                oliver INTEGER DEFAULT 0,
                fit_jack INTEGER DEFAULT 0,
                asmodeus INTEGER DEFAULT 0,
                hiromi INTEGER DEFAULT 0,
                last_boi TEXT
            )
        """)

        # insert values derived from 'old' table
        cursor.execute("""
            INSERT INTO boys_temp (user_id, mc, tom, oliver, fit_jack, asmodeus, hiromi, last_boi)
            SELECT
                user_id,
                CASE WHEN COALESCE(mc, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(tom, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(oliver, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(fit_jack, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(asmodeus, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(hiromi, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                last_boi
            FROM the_boys
        """)

        # drop old table
        cursor.execute("DROP TABLE the_boys")

        # rename 'new' table to oialt_harem
        cursor.execute("ALTER TABLE boys_temp RENAME TO the_boys")

        db.commit()

    except Exception as e:
        print(f"[the_boys to int] {e}")
    #endregion

    #region table li_potential to integer
    try:
        # create a temp table with the new type
        cursor.execute("""
            CREATE TABLE potlis_temp(
                user_id INTEGER,
                ava INTEGER DEFAULT 0,
                lilith INTEGER DEFAULT 0,
                fit_jack_groupie INTEGER DEFAULT 0,
                train_conductor INTEGER DEFAULT 0,
                shop_girl INTEGER DEFAULT 0,
                stone_elephant INTEGER DEFAULT 0,
                last_potential_li TEXT
            )
        """)

        # insert values derived from 'old' table
        cursor.execute("""
            INSERT INTO potlis_temp (user_id, ava, lilith, fit_jack_groupie, train_conductor, shop_girl, stone_elephant, last_potential_li)
            SELECT
                user_id,
                CASE WHEN COALESCE(ava, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(lilith, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(fit_jack_groupie, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(train_conductor, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(shop_girl, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(stone_elephant, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                last_potential_li
            FROM li_potential
        """)

        # drop old table
        cursor.execute("DROP TABLE li_potential")

        # rename 'new' table to oialt_harem
        cursor.execute("ALTER TABLE potlis_temp RENAME TO li_potential")

        db.commit()

    except Exception as e:
        print(f"[li_potential to int] {e}")
    #endregion

    #region table eternum_harem to integer
    try:
        # create a temp table with the new type
        cursor.execute("""
            CREATE TABLE eharem_temp(
                user_id INTEGER,
                alex INTEGER DEFAULT 0,
                annie INTEGER DEFAULT 0,
                dalia INTEGER DEFAULT 0,
                luna INTEGER DEFAULT 0,
                nancy INTEGER DEFAULT 0,
                nova INTEGER DEFAULT 0,
                penny INTEGER DEFAULT 0,
                last_girl TEXT,
                calypso INTEGER DEFAULT 0
            )
        """)

        # insert values derived from 'old' table
        cursor.execute("""
            INSERT INTO eharem_temp (user_id, alex, annie, dalia, luna, nancy, nova, penny, last_girl, calypso)
            SELECT
                user_id,
                CASE WHEN COALESCE(alex, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(annie, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(dalia, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(luna, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(nancy, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(nova, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(penny, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                last_girl,
                CASE WHEN COALESCE(calypso, 'NONE') = 'NONE' THEN 0 ELSE 1 END
            FROM eternum_harem
        """)

        # drop old table
        cursor.execute("DROP TABLE eternum_harem")

        # rename 'new' table to oialt_harem
        cursor.execute("ALTER TABLE eharem_temp RENAME TO eternum_harem")

        db.commit()

    except Exception as e:
        print(f"[eternum_harem to int] {e}")
    #endregion

    #region table homies to integer
    try:
        # create a temp table with the new type
        cursor.execute("""
            CREATE TABLE homies_temp(
                user_id INTEGER,
                chang INTEGER DEFAULT 0,
                chopchop INTEGER DEFAULT 0,
                victor INTEGER DEFAULT 0,
                jerry INTEGER DEFAULT 0,
                micaela INTEGER DEFAULT 0,
                noah INTEGER DEFAULT 0,
                orion INTEGER DEFAULT 0,
                raul INTEGER DEFAULT 0,
                last_homie TEXT
            )
        """)

        # insert values derived from 'old' table
        cursor.execute("""
            INSERT INTO homies_temp (user_id, chang, chopchop, victor, jerry, micaela, noah, orion, raul, last_homie)
            SELECT
                user_id,
                CASE WHEN COALESCE(chang, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(chopchop, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(victor, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(jerry, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(micaela, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(noah, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(orion, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(raul, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                last_homie
            FROM homies
        """)

        # drop old table
        cursor.execute("DROP TABLE homies")

        # rename 'new' table to oialt_harem
        cursor.execute("ALTER TABLE homies_temp RENAME TO homies")

        db.commit()

    except Exception as e:
        print(f"[homies to int] {e}")
    #endregion

    #region table side_girls to integer
    try:
        # create a temp table with the new type
        cursor.execute("""
            CREATE TABLE sides_temp(
                user_id INTEGER,
                bluefoxmaiden INTEGER DEFAULT 0,
                lorelei INTEGER DEFAULT 0,
                eva INTEGER DEFAULT 0,
                idriel INTEGER DEFAULT 0,
                maat INTEGER DEFAULT 0,
                redfoxmaiden INTEGER DEFAULT 0,
                wenlin INTEGER DEFAULT 0,
                last_affair TEXT
            )
        """)

        # insert values derived from 'old' table
        cursor.execute("""
            INSERT INTO sides_temp (user_id, bluefoxmaiden, lorelei, eva, idriel, maat, redfoxmaiden, wenlin, last_affair)
            SELECT
                user_id,
                CASE WHEN COALESCE(bluefoxmaiden, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(lorelei, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(eva, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(idriel, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(maat, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(redfoxmaiden, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(wenlin, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                last_affair
            FROM side_girls
        """)

        # drop old table
        cursor.execute("DROP TABLE side_girls")

        # rename 'new' table to oialt_harem
        cursor.execute("ALTER TABLE sides_temp RENAME TO side_girls")

        db.commit()

    except Exception as e:
        print(f"[side_girls to int] {e}")
    #endregion

    #region table creatures to integer
    try:
        # create a temp table with the new type
        cursor.execute("""
            CREATE TABLE pets_temp(
                user_id INTEGER,
                carolyn INTEGER DEFAULT 0,
                igor INTEGER DEFAULT 0,
                kermit INTEGER DEFAULT 0,
                mauricec INTEGER DEFAULT 0,
                mauriceg INTEGER DEFAULT 0,
                mauricet INTEGER DEFAULT 0,
                pancho INTEGER DEFAULT 0,
                last_creature TEXT
            )
        """)

        # insert values derived from 'old' table
        cursor.execute("""
            INSERT INTO pets_temp (user_id, carolyn, igor, kermit, mauricec, mauriceg, mauricet, pancho, last_creature)
            SELECT
                user_id,
                CASE WHEN COALESCE(carolyn, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(igor, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(kermit, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(mauricec, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(mauriceg, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(mauricet, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                CASE WHEN COALESCE(pancho, 'NONE') = 'NONE' THEN 0 ELSE 1 END,
                last_creature
            FROM creatures
        """)

        # drop old table
        cursor.execute("DROP TABLE creatures")

        # rename 'new' table to oialt_harem
        cursor.execute("ALTER TABLE pets_temp RENAME TO creatures")

        db.commit()

    except Exception as e:
        print(f"[creatures to int] {e}")
    #endregion

    #endregion

    db.commit()
    cursor.close()
    db.close()


def add_user():
    """Adds a decoy empty user to the test DB; No need for ID's because the system tracks autoincrements automatically."""

    global test_id

    db = sqlite3.connect(FakeClient.db_path)
    cursor = db.cursor()

    cursor.execute("INSERT INTO users (discord_id) VALUES (?)", [test_id])
    tables = [ 
        "eternum", "eternum_harem", "homies", "side_girls", "creatures"
    ]

    for table in tables:
        cursor.execute("INSERT INTO %s (user_id) VALUES (?)" % table, [test_id])

    db.commit()
    cursor.close()
    db.close()

    test_id += 1

    return (test_id - 1)


def cleanse_db():
    """Removes all entries from the test database."""

    db = sqlite3.connect(FakeClient.db_path)
    cursor = db.cursor()

    cursor.execute("DELETE FROM creatures")
    cursor.execute("DELETE FROM eternum")
    cursor.execute("DELETE FROM eternum_harem")
    cursor.execute("DELETE FROM homies")
    cursor.execute("DELETE FROM li_potential")
    cursor.execute("DELETE FROM oialt")
    cursor.execute("DELETE FROM oialt_harem")
    cursor.execute("DELETE FROM side_girls")
    cursor.execute("DELETE FROM stabby_mikes")
    cursor.execute("DELETE FROM the_boys")
    cursor.execute("DELETE FROM users")

    db.commit()
    cursor.close()
    db.close()


async def reset_table(table: str):
    """Resets all entries in a given table to default values."""
    db = sqlite3.connect(FakeClient.db_path)
    cursor = db.cursor()

    # get all columns' names and default values
    cursor.execute(f"PRAGMA table_info('{table}')")
    for col in cursor.fetchall():
        # skip user ID col reset
        if col[1] == "user_id":
            continue

        # update each entry of every column to its default value.
        cursor.execute("UPDATE %s SET %s=?" % (table, col[1]), [col[4]])

    db.commit()
    cursor.close()
    db.close()


async def deprotect(protector: str, uid: int):
    """Removes a specific protection for a given user"""
    db = sqlite3.connect(FakeClient.db_path)
    cursor = db.cursor()
    
    cursor.execute("UPDATE eternum SET %s = 0 WHERE user_id=?" % protector, [uid])

    db.commit()
    cursor.close()
    db.close()


@pytest.fixture(scope="session")
def eternum():
    client = FakeClient()

    createAndUpdateDatabase()
    cleanse_db()

    yield Eternum(client)
    
    cleanse_db()

class TestEternum():
    @staticmethod
    async def get_protector(effect: Effects) -> Effects:
        """Returns the character card of the protector that thwarts a given villain."""
        if effect == Effects.HAREM_KILLER:
            return Effects.HAREM_SAVIOUR

        if effect == Effects.SIDE_GIRL_KIDNAPPER:
            return Effects.SIDE_GIRL_SAVIOUR

        if effect == Effects.HOMIE_KILLER:
            return Effects.HOMIE_SAVIOUR

        if effect == Effects.CREATURE_STOMPER:
            return Effects.CREATURE_SAVIOUR

    @staticmethod
    async def get_preferred(effect: Effects, eternum) -> CharacterCard:
        """Returns the character card of a villain's preferred target."""
        if effect == Effects.HAREM_KILLER:
            return await eternum.characterList.getCharacter("Alexandra")

        if effect == Effects.SIDE_GIRL_KIDNAPPER:
            return None

        if effect == Effects.HOMIE_KILLER:
            return await eternum.characterList.getCharacter("Jerry")

        if effect == Effects.CREATURE_STOMPER:
            return await eternum.characterList.getCharacter("Kermit")

    @staticmethod
    async def get_random_target(effect: Effects, eternum) -> CharacterCard:
        """Returns the character card of a villain's non-preferential target."""
        if effect == Effects.HAREM_KILLER:
            return await eternum.characterList.getCharacter("Dalia")

        if effect == Effects.SIDE_GIRL_KIDNAPPER:
            return await eternum.characterList.getCharacter("Maat")

        if effect == Effects.HOMIE_KILLER:
            return await eternum.characterList.getCharacter("Victor")

        if effect == Effects.CREATURE_STOMPER:
            return await eternum.characterList.getCharacter("Maurice")

    @staticmethod
    async def get_effecting_collection(effect: Effects) -> Collections:
        """Returns the collection affected when a villain acts."""
        if effect == Effects.HAREM_KILLER:
            return Collections.HAREM

        if effect == Effects.SIDE_GIRL_KIDNAPPER:
            return Collections.SIDE_DISHES

        if effect == Effects.HOMIE_KILLER:
            return Collections.THE_HOMIES

        if effect == Effects.CREATURE_STOMPER:
            return Collections.CREATURES

    @staticmethod
    async def assert_collectible(uid: int, chara: str, table: str) -> bool:
        db = sqlite3.connect(FakeClient.db_path)
        cursor = db.cursor()

        cursor.execute("SELECT %s FROM %s WHERE user_id=?" % (chara, table), [uid])
        val = cursor.fetchone()

        cursor.close()
        db.close()

        return bool(val[0])


    @pytest.mark.asyncio
    async def test_collectibles(self, eternum):
        print("---------------------------\n----------TEST_COLLECTIBLES----------\n---------------------------")

        # add a new user
        uid = add_user()

        #------------------------------------------------------+
        #               [C O L L E C T I B L E S]              |
        #------------------------------------------------------+

        # foreach collectible try adding it twice (check duplicate value)
        for i in range(1, len(Collections)):
            print(f"----------\nTesting collection {Collections(i)}")
            collectibles = await eternum.characterList.getCollectiblesOfType(Collections(i))

            for chara in collectibles:
                # first time obtention; shouldn't be duplicate but should figure in the table
                results1 = await eternum.updateDatabase(uid=uid, character=chara)
                assert(not results1.duplicate)
                assert(TestEternum.assert_collectible(uid, chara.filename, chara.collection.table()))

                # should be duplicate and still figure in the table.
                results2 = await eternum.updateDatabase(uid=uid, character=chara)
                assert(results2.duplicate)
                assert(TestEternum.assert_collectible(uid, chara.filename, chara.collection.table()))

            await reset_table(Collections(i).table)

    @pytest.mark.asyncio
    async def test_villains(self, eternum):
        print("---------------------------\n----------TEST_VILLAINS----------\n---------------------------")

        # add a new user
        uid = add_user()
        
        #----------------------------------------------+
        #               [V I L L A I N S]              |
        #----------------------------------------------+
        
        # start at 1 to skip Effects.NONE
        for i in range(1, len(Effects)):

            effect = Effects(i)
            # skip even enum members (saviours) - implicitly tested either way.
            if i % 2 == 1:
                continue
            
            print(f"----------\nTesting villain {Effects(i)}")
            temp = await eternum.characterList.getEffectorsOfType(effect)
            villain = temp[0]
            assert(isinstance(villain, Villain))
            
            temp = await eternum.characterList.getEffectorsOfType(await TestEternum.get_protector(effect))
            protector = temp[0]
            assert(isinstance(protector, CharacterCard))

            pref_target = await TestEternum.get_preferred(effect, eternum)
            # target may be none (Axel) so no assert here

            other_target = await TestEternum.get_random_target(effect, eternum)
            assert(isinstance(other_target, CharacterCard))

            collection = await TestEternum.get_effecting_collection(effect)

            # reset all affected tables just in case
            await reset_table('eternum')
            await reset_table(collection.table())

            
            print(f"-----\nTesting roster:\nvillain: {villain.name}\nprotector: {protector.name}\npreferred target: {'None' if pref_target is None else pref_target.name}\nother target: {other_target.name}")

            #------------------------------------------------------------+
            #---------------case unprotected without target--------------|
            #------------------------------------------------------------+

            # add villain; should flag as denied (protected) and victim should be named.
            results2 = await eternum.updateDatabase(uid=uid, character=villain)
            print(f"-----\nduplicate: {results2.duplicate}; protected: {results2.protected}; victim: {'None' if results2.victim is None else results2.victim}.")
            assert(not results2.protected)
            assert(results2.victim == "Nobody")

            #-------------------------------------------+
            #---------------case protected--------------|
            #-------------------------------------------+

            # add a potential victim (protection doesn't trigger if no victim)
            await eternum.updateDatabase(uid=uid, character=other_target)
            assert(await TestEternum.assert_collectible(uid, other_target.filename, other_target.collection.table()))

            # add protector; should flag as protected and figure in the 'eternum' table.
            results1 = await eternum.updateDatabase(uid=uid, character=protector)
            print(f"-----\nduplicate: {results1.duplicate}; protected: {results1.protected}; victim: {'None' if results1.victim is None else results1.victim}.")
            assert(results1.protected)
            assert(await TestEternum.assert_collectible(uid, protector.filename, 'eternum'))

            # add villain; should flag as denied (protected) and victim should be named. Collectible should still be in table.
            results2 = await eternum.updateDatabase(uid=uid, character=villain)
            print(f"-----\nduplicate: {results2.duplicate}; protected: {results2.protected}; victim: {'None' if results2.victim is None else results2.victim}.")
            assert(results2.protected)
            assert(results2.victim != "Nobody")
            assert(await TestEternum.assert_collectible(uid, other_target.filename, other_target.collection.table()))
            
            #----------------------------------------------------------------------+
            #---------------case unprotected with preferential target--------------|
            #----------------------------------------------------------------------+

            # skip case Axel (no preferential target)
            if pref_target is not None:
                # add both the preferential and non-preferential, and check that the victim is the preferential one.
                # non-preferential last to account for scenario of villain checking last obtained collectible.
                await eternum.updateDatabase(uid=uid, character=pref_target)
                await eternum.updateDatabase(uid=uid, character=other_target)

                # both characters should be in the database
                assert(await TestEternum.assert_collectible(uid, pref_target.filename, pref_target.collection.table()))
                assert(await TestEternum.assert_collectible(uid, other_target.filename, other_target.collection.table()))

                # should be flagged as successful with victim == pref_target.name; Table should contain other_target but not pref_target.
                results2 = await eternum.updateDatabase(uid=uid, character=villain)
                print(f"-----\nduplicate: {results2.duplicate}; protected: {results2.protected}; victim: {'None' if results2.victim is None else results2.victim}.")
                assert(not results2.protected)
                assert(results2.victim == pref_target.name)
                assert(not await TestEternum.assert_collectible(uid, pref_target.filename, pref_target.collection.table()) and 
                       await TestEternum.assert_collectible(uid, other_target.filename, other_target.collection.table()))
                
            #-------------------------------------------------------------------------+
            #---------------case unprotected without preferential target--------------|
            #-------------------------------------------------------------------------+

            # loop through options maybe here instead of just 1 lol to avoid missing out on faulty DB names
            for chara in collection.members():
                card = await eternum.characterList.getCharacterWithFilename(chara)

                await eternum.updateDatabase(uid=uid, character=card)
                assert(await TestEternum.assert_collectible(uid, card.filename, card.collection.table()))
                
                # remove protection in scenario victim is also protector (Calypso).
                if card.name == protector.name:
                    print("Calypso case triggered.")
                    await deprotect(card.filename, uid)

                # should be flagged as successful with victim == other_target.name; other_target shouldn't be in the table anymore.
                results2 = await eternum.updateDatabase(uid=uid, character=villain)
                print(f"-----\nduplicate: {results2.duplicate}; protected: {results2.protected}; victim: {'None' if results2.victim is None else results2.victim}.")
                assert(not results2.protected)
                assert(results2.victim == card.name)
                assert(not await TestEternum.assert_collectible(uid, card.filename, card.collection.table()))


    def test_collections(self):
        # run the -ecollections command and check against DB entries
        assert(True)

    def test_eharem(self):
        # run the eharem command and compare get- and misslists
        assert(True)

    def test_sidegirls(self):
        # run -sidegirls command and compare get- and misslists
        assert(True)

    def test_ehomies(self):
        # run -homies command and compare get- and misslists
        assert(True)

    def test_pets(self):
        # run -creatures command and compare get- and misslists
        assert(True)

    def test_protectors(self):
        # run -eprotectors command and compare get- and misslists
        assert(True)
