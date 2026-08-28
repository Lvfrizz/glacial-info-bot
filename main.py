import discord
from discord.ext import commands
from discord import app_commands
import os

# ==================== CONFIG ====================
TOKEN = os.getenv("DISCORD_TOKEN")
GLACIAL_COLOR = 0x7FDBFF

# ==================== SERVER INFO ====================
INFO = {
    "custom_drops": {
        "title": "📦 Custom Drops",
        "description": (
            "**│ White Drops**\nFull Flak Kit, tools, Kibble and empty Cryopods\n"
            "**✦ White Ring Drops**\nSame but Higher BP %\n\n"
            "**│ Green Drops**\nMetal Building Kit\n"
            "**✦ Green Ring Drops**\nCrafting kit\n\n"
            "**│ Blue Drops**\nPVP Kit (shotgun, bolas, crossbow, ammo, Rockets)\n"
            "**✦ Blue Ring Drops**\nSame but Higher BP %\n\n"
            "**│ Purple Drops**\nRandom Dino Saddles\n"
            "**✦ Purple Ring Drops**\nSame but Higher BP % and Tek saddles\n\n"
            "**│ Yellow Drops**\nARB Bullets, Electronics, Silica Pearls\n"
            "**✦ Yellow Ring Drops**\nElement Shards, Black Pearls, Polymer\n\n"
            "**│ Red Drops**\n6 Random Chibis, Element\n"
            "**✦ Red Ring Drops**\nElement, Random Tek Suit piece, Tek Rep"
        )
    },
    "orbital_drops": {
        "title": "🛰️ Orbital Drops",
        "description": (
            "**Blue OSD**\nSaddles, Tek, Materials, Regular Weapons / BPs\n\n"
            "**Yellow OSD**\nSaddles, Tek Materials, Flak / Tek\n\n"
            "**Red OSD**\nSaddles / BPs, Tek / Riot BP%, Materials\n\n"
            "**Purple OSD**\nSaddles / BPs, Tek / Riot BP%, Materials"
        )
    },
    "modded_crafts": {
        "title": "🛠️ Modded Crafts",
        "description": (
            "**Simplified Recipes:**\n\n"
            "⬩➤ **Cement Paste** → Rocks\n"
            "⬩➤ **Electronics** → Silica Pearls\n"
            "⬩➤ **Gunpowder** → Sparkpowder\n"
            "⬩➤ **Polymer** → Cementing Paste\n"
            "⬩➤ **Sparkpowder** → Cement Paste"
        )
    },
    "bosses": {
        "title": "🦖 Bosses Drops",
        "description": (
            "**Gamma**\n• Black Pearl: 250-1000\n• Element: 250-1000\n• Tek + Metal: 1000-2500\n• Polymer: 250-1500\n*(Trophy & Flag included)*\n\n"
            "**Beta**\n• Black Pearl: 500-1500\n• Element: 500-1500\n• Tek + Metal: 1500-3000\n• Polymer: 500-2000\n*(Trophy & Flag included)*\n\n"
            "**Alpha**\n• Black Pearl: 1000-2500\n• Element: 1000-2500\n• Tek + Metal: 2500-3500\n• Polymer: 1000-2500\n*(Trophy & Flag included)*"
        )
    },
    "mods": {
        "title": "📜 Cluster Mod List",
        "description": (
            "• Helena\n• Cybers Structures\n• Pelayoris Cryop Storage\n• ARKomatic\n• ASE HatchFrames plus\n"
            "• Just want Cuddles\n• Tribute and Element transfer\n• Safe OSD & Element veins\n• Cheat Prevention\n"
            "• Der Dino Find\n• Awesome Spy Glass\n• ASA Bot companion\n• Tip4Serv Shop Mod\n• Magas Shop ingame\n"
            "• Solo farm mod\n• Creature Management tool\n• White Flag\n• Automated ARK\n• Dino Color tokens\n"
            "• World Builder\n• Helena Bot companion\n• Automated Dino Wipes\n• Player Renamer\n• FPS Bot Booster"
        )
    },
    "stats": {
        "title": "📊 Player & Dino Stats",
        "description": (
            "**Player Stats**\n"
            "• HP = **50x**\n"
            "• Stamina = **50x**\n"
            "• Oxygen = **50x**\n"
            "• Food = Does not go down\n"
            "• Water = Does not go down\n"
            "• Weight = **120x**\n"
            "• Damage = **15x**\n"
            "• Speed = **9x**\n"
            "• Fortitude = **100x**\n"
            "• Crafting = **100000x**\n\n"
            "**Tamed Dino Stats**\n"
            "• HP = **25x**\n"
            "• Stamina = **50x**\n"
            "• Weight = **10000x**\n"
            "• Damage = **15x**\n"
            "• Speed = **1.5x** *(enabled on all flying dinos)*\n\n"
            "**Nerfed Dinos**\n"
            "• Acros\n"
            "• Astrocetus (Space Whale)\n"
            "• Aureliax\n"
            "• Deinosuchus\n"
            "• Dreadnoughtus\n"
            "• Elderclaw\n"
            "• Gigadesmodus\n"
            "• Griffin *(slightly)*\n"
            "• Lumina\n"
            "• Magmasaur\n"
            "• Megachelon\n"
            "• Mek\n"
            "• Umbra\n"
            "• Veilwyn\n\n"
            "**Blocked from Spawning** *(for better performance)*\n"
            "• Compys\n"
            "• Ark Fish\n"
            "• Pegomastax"
        )
    }
}

# ==================== RULES ====================
RULES = {
    "discord": {
        "title": "💬 Discord Rules",
        "description": (
            "**1 • Player Registration**\n"
            "All active players must register their in-game name and tribe name in the designated registration channel.\n\n"
            "**2 • Zero Tolerance Policy – Harassment & Hate**\n"
            "Racism, hate speech, discrimination, harassment, or targeted toxicity based on race, religion, gender, sexuality, nationality, or personal beliefs is strictly prohibited.\n\n"
            "**Punishment Scale:**\n"
            "• 1st Violation → Server Mute\n"
            "• 2nd Violation → 3-Day Temporary Ban\n"
            "• 3rd Violation → Permanent Ban\n"
            "Staff reserve the right to escalate punishments immediately for severe or repeated offenses.\n\n"
            "**3 • Channel Usage**\n"
            "Please use channels for their intended purpose. Repeated misuse may result in a mute or further action.\n\n"
            "**4 • Community Conduct & Toxicity**\n"
            "Competitive banter is expected and encouraged, but excessive salt, drama, or toxicity that negatively impacts the community will not be tolerated.\n\n"
            "**5 • Content Restrictions**\n"
            "No NSFW, inappropriate, explicit, or highly offensive images, videos, memes, or links.\n\n"
            "**6 • Base Coordinates**\n"
            "Do not post or share another tribe’s base coordinates, screenshots of their builds, or any sensitive information in public channels.\n\n"
            "**7 • Support & Reporting**\n"
            "All server issues, rule violations, complaints, and support requests must be handled through the ticket system.\n\n"
            "**8 • Privacy**\n"
            "Sharing or leaking any personal information about other players is strictly forbidden.\n\n"
            "**9 • Spam & Flooding**\n"
            "No spamming, message flooding, excessive tagging, or unnecessary caps.\n\n"
            "**10 • Player Recruitment**\n"
            "Do not intentionally invite players whose main purpose is to cause disruption, drama, or harm to the server.\n\n"
            "**11 • Respect Towards Staff**\n"
            "Treat staff with respect. Disrespect or backtalk will not be tolerated.\n\n"
            "**Final Note:** These rules ensure a fun, competitive, and respectful environment. Staff decisions are final."
        )
    },
    "general": {
        "title": "📜 Cluster General Rules",
        "description": (
            "• No cheating, exploiting, or using unintended game mechanics.\n"
            "• No meshing or building inside the mesh.\n"
            "• No duplication of items, creatures, or resources.\n"
            "• No box raiding. Players may be boxed in (1x1), but tames must remain damageable. (Same applies to CS Tek Shield on any Dino Plat saddle)\n"
            "• No tunneling beneath enemy structures to bypass defenses.\n"
            "• Do not leave breeding creatures unattended. Excessive eggs, babies, or breeding clutter may be removed by staff.\n"
            "• Turrets may not be placed on boats, rafts, or creatures.\n"
            "• No insiding. Betraying your tribe or alliance for personal gain is prohibited.\n"
            "• Admin structures may not be damaged unless specifically designated as raid targets.\n"
            "• No Bob Raiding (let them be happy lol)"
        )
    },
    "tribe": {
        "title": "👥 Tribe & Alliance Rules",
        "description": (
            "1. Maximum tribe size is **6 players**.\n"
            "2. Only **one alliance** is permitted.\n"
            "3. Alliance members may assist in raids and defenses.\n"
            "*(Allies cannot participate in raids on **small tribes**. A small tribe is **1–4 registered members**.)*\n\n"
            "4. No tribe cycling or alliance cycling. A minimum **24-hour waiting period** is required before joining a new tribe or alliance.\n"
            "5. Tribe or alliance changes may not occur during, immediately before, or immediately after a raid.\n"
            "6. Tribe rosters must match the Tribe Registry.\n"
            "7. Tribe names, players, and alliances must be the same across all maps.\n"
            "8. No teaming with players or tribes outside of your registered alliance during raids, defenses, scouting, or PvP.\n"
            "9. Temporary alliances or “helping friends” during PvP is considered teaming and is not allowed.\n"
            "10. If any tribe name, players, or alliances change, they must be updated on the Tribe Registration."
        )
    },
    "building": {
        "title": "🏰 Building & Base Rules",
        "description": (
            "1. Maximum of **3 bases** (1 main) per map and **4 TPs**.\n"
            "2. After a raid is completed or abandoned, raid structures must be removed or converted into a legitimate base (or notify admin to wipe leftover spam).\n"
            "3. Cave edits and donations are **non-refundable**.\n"
            "4. Purchased modded caves will be removed after you lose domination of the cave/area and cannot be replaced or refunded.\n"
            "5. Aggressive wandering creatures must be contained within a Dino Leash.\n"
            "6. Excessive spam that negatively impacts server performance must be removed if requested by staff.\n"
            "7. Structure spam is allowed (foundations only) in a moderated amount. Failure to control it may result in staff wiping the area to reduce lag."
        )
    },
    "whiteflag": {
        "title": "🏳️ White Flag Protection",
        "description": (
            "1. White Flag protection lasts **7 days** and cannot be extended.\n"
            "2. White Flag only protects your **main base**.\n"
            "3. Players under White Flag may PvP but may **not participate in raids** until protection expires (or is ended by the tribe owner).\n"
            "4. Violating White Flag rules will result in immediate loss of protection."
        )
    },
    "pvp": {
        "title": "⚔️ PvP / Raid Rules",
        "description": (
            "1. Third-party raiding is prohibited. Only the attacking and defending tribes/alliances may participate.\n"
            "*(Alliance attacking during a raid on **small tribes** is not allowed. A small tribe is **1–4 registered members**.)*\n\n"
            "2. Thralls are only allowed for PvE (bosses, exploring, etc.). They may not be used for raiding, defending, or PvP (small 1-2 man tribes may request admin permission).\n"
            "3. No Cannon raiding.\n\n"
            "**4. Space Whale Rules**\n"
            "• Excluded from the propagator and unbreedable.\n"
            "• Building on the back/platform is not permitted.\n"
            "• Further adjustments may be made based on feedback.\n\n"
            "5. Using any creature abilities, structures, or effects to become fully invisible during PvP is strictly prohibited (including Space Whale burrowing and any builds that conceal the player).\n"
            "6. Spamming in FOBs is not allowed.\n"
            "7. Meks must not mesh unless clearing a meshed structure.\n"
            "8. Donations are not allowed mid-raid.\n"
            "9. Popcorning / uploading / destroying or taking loot during a raid is not allowed."
        )
    },
    "donations": {
        "title": "💰 Donations Rules",
        "description": (
            "• **All Sales Are Final** — No refunds once delivered (except clear technical errors on our side).\n"
            "• **Delivery Time** — Most packages arrive within 5–15 minutes. Open a ticket if not received within 30 minutes.\n"
            "• **One Character Only** — Purchased items are for one character only (unless character loss).\n"
            "• **No Reselling** of packages.\n\n"
            "**Cave Edits / Custom Entrances**\n"
            "• Permanent once placed.\n"
            "• You are responsible for providing correct location/details.\n"
            "• Cannot be moved or refunded after completion.\n"
            "• Abusing cave edits will result in removal + possible punishment.\n\n"
            "• Make sure you are on the correct character when purchasing.\n"
            "• Buying packages does not give immunity from server rules.\n"
            "• Any chargeback results in a permanent ban and loss of all items.\n"
            "• Need help? Open a support ticket.\n"
            "• Donations are not allowed mid-raid."
        )
    },
    "extra": {
        "title": "📌 Extra Rules & Warning System",
        "description": (
            "**Extra Rules**\n"
            "• Selling bases, creatures, items, tribe ownership, or services for real-world money is strictly prohibited.\n"
            "• **Max 15 uncryo’d dinos per base.** Dinos set to Aggressive, Neutral, or Wandering must be contained within a Dino Leash (**max 4 dinos per leash**).\n"
            "• CS Medical Stations may only be used for healing during **breeding**. They are **not** allowed during raids or defending.\n"
            "• If you are defending a modded entry with a dino, you **must be riding the dino**. Do not block or exploit modded entries with dinos/creatures.\n"
            "• One main account per player. Alts are not allowed for extra tribe slots, extra White Flags, extra shop purchases, or extra PvP presence.\n"
            "• TPs cannot be hidden inside enemy render, used to drop into someone else’s base, or placed in a way that bypasses cave/modded entries.\n"
            "• Do not use World Builder volumes, doors, or edits to trap players, hide hitboxes, or create unraidable geometry.\n"
            "• Excessive carpet turrets or spam may be wiped by staff if not cleared by the tribe.\n\n"
            "**Warning & Strike System**\n\n"
            "ㆍ **Verbal / Soft Warning** → Logged with Helena\n"
            "ㆍ **1st Strike** → Official written warning + logged\n"
            "ㆍ **2nd Strike** → Heavier restriction or temporary ban\n"
            "ㆍ **3rd Strike** → Long ban or permanent\n\n"
            "**Minor** (Soft Warning / Strike 1)\n"
            "Toxic chat, minor rule bending, ignoring admin once, leaving clutter after leaving tribe\n\n"
            "**Medium** (Strike 1 or 2)\n"
            "Excessive griefing, repeated toxicity, exploiting after warning, drama baiting, shop abuse\n\n"
            "**Severe** (Strike 2/3 or instant ban)\n"
            "RMT, duping, racism, ban evasion, IRL threats, intentionally crashing the server\n\n"
            "**Final Note:** Staff decisions are final. Breaking rules may result in warnings, temporary bans, or permanent bans depending on severity."
        )
    }
}

# ==================== SELECT MENUS ====================
class InfoSelect(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Custom Drops", value="custom_drops", emoji="📦"),
            discord.SelectOption(label="Orbital Drops", value="orbital_drops", emoji="🛰️"),
            discord.SelectOption(label="Modded Crafts", value="modded_crafts", emoji="🛠️"),
            discord.SelectOption(label="Bosses", value="bosses", emoji="🦖"),
            discord.SelectOption(label="Mods List", value="mods", emoji="📜"),
            discord.SelectOption(label="Player & Dino Stats", value="stats", emoji="📊"),
        ]
        super().__init__(placeholder="Choose a category...", options=options, custom_id="glacial_info_select")

    async def callback(self, interaction: discord.Interaction):
        data = INFO[self.values[0]]
        embed = discord.Embed(title=data["title"], description=data["description"], color=GLACIAL_COLOR)
        embed.set_footer(text="Glacial Ascent 50x • Info Panel")
        await interaction.response.send_message(embed=embed, ephemeral=True)


class RulesSelect(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Discord Rules", value="discord", emoji="💬"),
            discord.SelectOption(label="General Rules", value="general", emoji="📜"),
            discord.SelectOption(label="Tribe & Alliance", value="tribe", emoji="👥"),
            discord.SelectOption(label="Building & Base", value="building", emoji="🏰"),
            discord.SelectOption(label="White Flag", value="whiteflag", emoji="🏳️"),
            discord.SelectOption(label="PvP / Raid Rules", value="pvp", emoji="⚔️"),
            discord.SelectOption(label="Donations Rules", value="donations", emoji="💰"),
            discord.SelectOption(label="Extra + Strikes", value="extra", emoji="📌"),
        ]
        super().__init__(placeholder="Choose a rules category...", options=options, custom_id="glacial_rules_select")

    async def callback(self, interaction: discord.Interaction):
        data = RULES[self.values[0]]
        embed = discord.Embed(title=data["title"], description=data["description"], color=GLACIAL_COLOR)
        embed.set_footer(text="Glacial Ascent 50x • Rules")
        await interaction.response.send_message(embed=embed, ephemeral=True)


class InfoView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(InfoSelect())


class RulesView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(RulesSelect())


# ==================== BOT ====================
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    bot.add_view(InfoView())
    bot.add_view(RulesView())
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)


@bot.tree.command(name="setup_panel", description="Post the Server Info panel")
@app_commands.checks.has_permissions(administrator=True)
async def setup_panel(interaction: discord.Interaction):
    embed = discord.Embed(
        title="❄️ GLACIAL ASCENT SERVER INFO",
        description=(
            "**INFO UPDATES CONSTANTLY**\n\n"
            "Click the dropdown below to view detailed server information!\n\n"
            "**Maps:** The Island • The Center • Ragnarok • Aberration • Extinction • Valguero • Astraeos • Lost Colony • Genesis Part 1"
        ),
        color=GLACIAL_COLOR
    )
    embed.set_footer(text="Glacial Ascent 50x")
    await interaction.response.send_message(embed=embed, view=InfoView())


@bot.tree.command(name="rules", description="Post the Cluster Rules panel")
@app_commands.checks.has_permissions(administrator=True)
async def rules(interaction: discord.Interaction):
    embed = discord.Embed(
        title="❄️ GLACIAL ASCENT RULES",
        description="Click the dropdown below to view the different rule categories.\n\nPlease read carefully.",
        color=GLACIAL_COLOR
    )
    embed.set_footer(text="Glacial Ascent 50x • Staff decisions are final")
    await interaction.response.send_message(embed=embed, view=RulesView())


@setup_panel.error
@rules.error
async def permission_error(interaction: discord.Interaction, error):
    if isinstance(error, app_commands.MissingPermissions):
        await interaction.response.send_message("You need Administrator permission.", ephemeral=True)


bot.run(TOKEN)
