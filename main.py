import discord
from discord.ext import commands
from discord import app_commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")
GLACIAL_COLOR = 0x7FDBFF

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
            "**Player Stats**\n• HP = **50x**\n• Stamina = **50x**\n• Oxygen = **50x**\n"
            "• Food = Does not go down\n• Water = Does not go down\n• Weight = **120x**\n"
            "• Damage = **15x**\n• Speed = **9x**\n• Fortitude = **100x**\n• Crafting = **100000x**\n\n"
            "**Tamed Dino Stats**\n• HP = **25x**\n• Stamina = **50x**\n• Weight = **10000x**\n"
            "• Damage = **15x**\n• Speed = **1.5x** *(enabled on all flying dinos)*"
        )
    },
    "nerfed_banned": {
        "title": "🚫 Nerfed & Banned Dinos",
        "description": (
            "**Nerfed Dinos**\n"
            "• Acros\n• Aureliax\n• Boaratos\n• Deinosuchus\n• Dreadnoughtus\n"
            "• Elderclaw\n• Gigadesmodus\n• Griffin *(slightly)*\n• Lumina\n"
            "• Magmasaur\n• Megachelon\n• Mek\n• Umbra\n• Veilwyn\n\n"
            "**Banned from Spawning / Using** *(for better performance)*\n"
            "• Compys\n• Ark Fish\n• Pegomastax\n• **Astrocetus (Space Whale)**"
        )
    }
}

RULES = {
    "discord": {
        "title": "💬 Discord Rules",
        "description": (
            "**1 • Player Registration**\nAll active players must register their in-game name and tribe name in the designated registration channel.\n\n"
            "**2 • Zero Tolerance Policy – Harassment & Hate**\nRacism, hate speech, discrimination, harassment, or targeted toxicity based on race, religion, gender, sexuality, nationality, or personal beliefs is strictly prohibited.\n\n"
            "**Punishment Scale:**\n• 1st Violation → Server Mute\n• 2nd Violation → 3-Day Temporary Ban\n• 3rd Violation → Permanent Ban\nStaff reserve the right to escalate punishments immediately for severe or repeated offenses.\n\n"
            "**3 • Channel Usage**\nPlease use channels for their intended purpose. Repeated misuse may result in a mute or further action.\n\n"
            "**4 • Community Conduct & Toxicity**\nCompetitive banter is expected and encouraged, but excessive salt, drama, or toxicity that negatively impacts the community will not be tolerated.\n\n"
            "**5 • Content Restrictions**\nNo NSFW, inappropriate, explicit, or highly offensive images, videos, memes, or links.\n\n"
            "**6 • Base Coordinates**\nDo not post or share another tribe’s base coordinates, screenshots of their builds, or any sensitive information in public channels.\n\n"
            "**7 • Support & Reporting**\nAll server issues, rule violations, complaints, and support requests must be handled through the ticket system.\n\n"
            "**8 • Privacy**\nSharing or leaking any personal information about other players is strictly forbidden.\n\n"
            "**9 • Spam & Flooding**\nNo spamming, message flooding, excessive tagging, or unnecessary caps.\n\n"
            "**10 • Player Recruitment**\nDo not intentionally invite players whose main purpose is to cause disruption, drama, or harm to the server.\n\n"
            "**11 • Respect Towards Staff**\nTreat staff with respect. Disrespect or backtalk will not be tolerated.\n\n"
            "• **Do not @ admins for any situation or tickets.**\n\n"
            "**Final Note:** These rules ensure a fun, competitive, and respectful environment. Staff decisions are final."
        )
    },
    "general": {
        "title": "📜 Cluster General Rules",
        "description": (
            "• No cheating, exploiting, or using unintended game mechanics.\n"
            "• No meshing or building inside the mesh.\n"
            "• No duplication of items, creatures, or resources.\n"
            "• **No box raiding.** Players may be boxed in (1x1), **tames must remain damageable**, (same goes to **Vehicles / Utility items / objects** — can't have structures on them or be used for raids).\n"
            "• No tunneling beneath enemy structures to bypass defenses.\n"
            "• Do not leave breeding creatures unattended. Excessive eggs, babies, or breeding clutter may be removed by staff.\n"
            "• Turrets may not be placed on boats, rafts, or creatures.\n"
            "• No insiding. Betraying your tribe or alliance for personal gain is prohibited.\n"
            "• Admin structures may not be damaged unless specifically designated as raid targets.\n"
            "• No Bob Raiding (let them be happy lol)\n\n"
            "• **One main account per player.** Alts are not allowed for extra tribe slots, extra White Flags, extra shop purchases, or extra PvP presence."
        )
    },
    "tribe": {
        "title": "👥 Tribe & Alliance Rules",
        "description": (
            "1. Maximum tribe size is **6 players**.\n2. Only **one alliance** is permitted.\n\n"
            "3. No tribe cycling or alliance cycling. A minimum **24-hour waiting period** is required before joining a new tribe or alliance.\n"
            "4. Tribe or alliance changes may not occur during, immediately before, or immediately after a raid. A **24-hour wait** is required after a raid ends before any tribe or alliance change.\n"
            "5. Tribe rosters must match the Tribe Registry.\n6. Tribe names, players, and alliances must be the same across all maps.\n"
            "7. No teaming with players or tribes outside of your registered alliance during raids, defenses, scouting, or PvP.\n"
            "8. Temporary alliances or “helping friends” during PvP is considered teaming and is not allowed.\n"
            "9. If any tribe name, players, or alliances change, they must be updated on the Tribe Registration."
        )
    },
    "building": {
        "title": "🏰 Building & Base Rules",
        "description": (
            "1. **Maximum of 4 bases per tribe across the entire cluster and 4 TPs per map.**\n"
            "2. After a raid is completed or abandoned, raid structures must be removed or converted into a legitimate base (or notify admin to wipe leftover spam).\n"
            "3. Purchased modded caves will be removed after you lose domination of the cave/area and cannot be replaced or refunded.\n"
            "4. Aggressive wandering creatures must be contained within a Dino Leash.\n"
            "5. Excessive spam that negatively impacts server performance must be removed if requested by staff.\n"
            "6. Structure spam is allowed (foundations only) in a moderated amount. Failure to control it may result in staff wiping the area to reduce lag.\n\n"
            "• **All uncryo’d dinos at base must be under leash, max of 5 dinos per leash.**\n\n"
            "• **If you are defending a modded entry with a dino, you must be riding the dino.** Do not block or exploit modded entries with dinos/creatures.\n\n"
            "• **TPs cannot be hidden inside enemy render, used to drop into someone else’s base, or placed in a way that bypasses cave/modded entries.**"
        )
    },
    "whiteflag": {
        "title": "🏳️ White Flag Protection",
        "description": (
            "1. White Flag protection lasts **7 days** and cannot be extended.\n"
            "2. White Flag only protects your **main base**.\n"
            "3. Players under White Flag may PvP but may **not participate in raids** until protection expires (or is ended by the tribe owner).\n"
            "4. Violating White Flag rules will result in immediate loss of protection.\n\n"
            "• **Tribes under White Flag can NOT place FOBs on any tribe until the grace period ends.**\n"
            "• **No tribe can place a FOB on tribes that are under White Flag until the grace period is done.**"
        )
    },
    "pvp": {
        "title": "⚔️ PvP / Raid Rules",
        "description": (
            "1. Third-party raiding is prohibited. Only the attacking and defending tribes/alliances may participate.\n\n"
            "2. **Alliances may participate in raids/defends if the tribe needs to equal numbers.**\n"
            "*(Example: if the tribe being attacked has 8 active players defending and you only have 4, your alliance may join to balance the numbers.)*\n\n"
            "3. Thralls are only allowed for PvE (bosses, exploring, etc.). They may not be used for raiding, defending, or PvP (small 1-2 man tribes may request admin permission).\n"
            "4. **Raft, zeppelin, cannons are not allowed during raids.**\n\n"
            "5. **Spam at FOB is allowed as long as it is to push to base. Foundations only.**\n"
            "6. Meks must not mesh unless clearing a meshed structure.\n"
            "7. Donations are not allowed mid-raid.\n"
            "8. Popcorning / uploading / destroying or taking loot during a raid is not allowed.\n\n"
            "• **CS Medical Stations** and **Home Sweet Home** may only be used for healing during **breeding**. They are **not** allowed during raids or defending.\n\n"
            "• **If you counter a FOB, you must take complete control of the raid.** Just destroying a FOB for fun or looking for PvP mid-raid **will count as third party.**\n\n"
            "• **Mass dino deployment during a raid to the point it affects server performance will not be allowed.**\n\n"
            "• **Using carts on dinos as extra protection during raids or defending is not allowed.**\n\n"
            "**FOB & Raid Rules**\n"
            "• **A FOB must stay active.** Active = soaking, destroying structures, killing players/tames, or clear tribe log activity.\n"
            "• **If a FOB has no activity for 24hrs, it becomes inactive and can be Admin AOE on request.**\n"
            "• **Only 1 active FOB per tribe per target base.**\n"
            "• **Once a raid ends, the FOB and all spam must be removed within 12 hrs.** Leaving permanent FOBs is not allowed.\n"
            "• **If your FOB is fully destroyed (or you pick it up / abandon it while under attack), you cannot place another FOB or start a new raid attempt on that same base for 24 hours.**\n"
            "• **Daily raid limit — 1 raid start per tribe per 24 hours.**\n"
            "• **No mid-raid tribe merges or “temporary” members.**\n"
            "• **Raiding the same tribe 3+ times in 7 days with no retaliation is considered griefing** (admin discretion + warning/wipe)."
        )
    },
    "harvest": {
        "title": "🌾 Custom Harvest Zones Rules",
        "description": (
            "「-✦ Custom Harvest Zones Rules ✦-」\n\n"
            "• No building permitted within a **30000 x 30000** range of the harvest zone.\n"
            "• TPs / FOBs are allowed within a **35000 x 35000** range, but **no turrets** are allowed.\n"
            "• **PvP is allowed** in these zones."
        )
    },
    "rathole": {
        "title": "🕳️ Rat Hole Rules",
        "description": (
            "• Building in known OP rat holes is strictly prohibited. This includes spots that are extremely hard or impossible to properly raid (such as the **Peli** rat hole and any similar mesh/underwater/tiny crevice spots).\n\n"
            "• Any structures placed in a banned rat hole will be wiped by staff. Repeat offenders will receive a strike.\n\n"
            "• **If unsure whether your spot is an illegal or legal rat hole, get in touch with admin on ticket for confirmation.**"
        )
    },
    "donations": {
        "title": "💰 Donations Rules",
        "description": (
            "• **All Sales Are Final** — No refunds once delivered (except clear technical errors on our side).\n"
            "• **Delivery Time** — Most packages arrive within 5–15 minutes. Open a ticket if not received within 30 minutes.\n"
            "• **One Character Only** — Purchased items are for one character only (unless character loss).\n"
            "• **No Reselling** of packages.\n\n**Cave Edits / Custom Entrances**\n• Permanent once placed.\n• You are responsible for providing correct location/details.\n• Cannot be moved or refunded after completion.\n• Abusing cave edits will result in removal + possible punishment.\n\n"
            "• Make sure you are on the correct character when purchasing.\n• Buying packages does not give immunity from server rules.\n"
            "• Any chargeback results in a permanent ban and loss of all items.\n• Need help? Open a support ticket.\n• Donations are not allowed mid-raid."
        )
    },
    "extra": {
        "title": "📌 Extra Rules & Warning System",
        "description": (
            "**Extra Rules**\n"
            "• Selling bases, creatures, items, tribe ownership, or services for real-world money is strictly prohibited.\n"
            "• Do not use World Builder volumes, doors, or edits to trap players, hide hitboxes, or create unraidable geometry.\n"
            "• Excessive carpet turrets or spam may be wiped by staff if not cleared by the tribe.\n\n"
            "**Warning & Strike System**\nㆍ **Verbal / Soft Warning** → Logged with Helena\nㆍ **1st Strike** → Official written warning + logged\nㆍ **2nd Strike** → Heavier restriction or temporary ban\nㆍ **3rd Strike** → Long ban or permanent\n\n"
            "**Minor** (Soft Warning / Strike 1)\nToxic chat, minor rule bending, ignoring admin once, leaving clutter after leaving tribe\n\n"
            "**Medium** (Strike 1 or 2)\nExcessive griefing, repeated toxicity, exploiting after warning, drama baiting, shop abuse\n\n"
            "**Severe** (Strike 2/3 or instant ban)\nRMT, duping, racism, ban evasion, IRL threats, intentionally crashing the server\n\n"
            "**Final Note:** Staff decisions are final."
        )
    }
}

RULES_ES = {
    "discord": {
        "title": "💬 Reglas de Discord",
        "description": (
            "**1 • Registro**\nRegistra tu nombre in-game y el de tu tribu.\n\n"
            "**2 • Cero tolerancia**\nNada de racismo, odio, acoso o discriminación.\n"
            "1ra falta → Mute • 2da → Ban 3 días • 3ra → Ban permanente.\n\n"
            "**3 • Canales**\nUsa cada canal para lo que es.\n**4 • Conducta**\nEl vacile está bien, el drama tóxico no.\n"
            "**5 • Contenido**\nNada NSFW/ofensivo.\n**6 • Coordenadas**\nNo publiques bases ajenas.\n"
            "**7 • Reportes**\nTodo por ticket.\n**8 • Privacidad**\nNada de datos personales.\n"
            "**9 • Spam**\nProhibido.\n**10 • Reclutamiento**\nNo invites gente solo para dañar el server.\n"
            "**11 • Staff**\nRespeta al staff. La decisión del staff es final.\n\n"
            "• **No @ a los admins para ninguna situación o tickets.**"
        )
    },
    "general": {
        "title": "📜 Reglas generales del cluster",
        "description": (
            "• Prohibido cheats, exploits o usar mecánicas no intencionadas del juego.\n"
            "• Prohibido meshear o buildear dentro del mesh.\n• Prohibido dupiar items, criaturas o recursos.\n"
            "• **No box raid.** Se puede boxear a un jugador en 1x1, **los tames tienen que poder recibir daño**, (lo mismo aplica a **Vehicles / Utility items / objetos** — no pueden tener structures encima ni usarse para raids).\n"
            "• Prohibido tunear por debajo de estructuras enemigas para saltarse defensas.\n"
            "• No dejes criaturas de breed sin atender. Huevos, babies o breed suelto en exceso lo puede borrar el staff.\n"
            "• Prohibido poner turrets en boats, rafts o criaturas.\n• Prohibido insidear.\n"
            "• No se pueden dañar estructuras de admin, salvo que estén marcadas como objetivo de raid.\n"
            "• No se raidea a bobs (déjalo disfrutar, jaja)\n\n"
            "• **Una cuenta main por jugador.** No alts para extra slots, White Flags, shop o PvP."
        )
    },
    "tribe": {
        "title": "👥 Reglas de Tribu y Alianza",
        "description": (
            "1. Máximo **6 jugadores** por tribu.\n2. Solo se permite **una alianza**.\n\n"
            "3. Prohibido tribe cycling o alliance cycling. Espera **mínimo 24 horas** antes de entrar a otra tribu o alianza.\n"
            "4. No se puede cambiar de tribu o alianza durante un raid, ni justo antes, ni justo después. Se requiere una espera de **24 horas** después de que termine un raid antes de cualquier cambio de tribu o alianza.\n"
            "5. El roster tiene que coincidir con el Tribe Registry.\n6. Nombre de tribu, jugadores y alianza iguales en todos los mapas.\n"
            "7. Prohibido teaming fuera de tu alianza registrada.\n8. “Ayudar a un pana” en PvP cuenta como teaming.\n"
            "9. Si cambia el nombre de la tribu, los jugadores o la alianza, actualízalo en el registro."
        )
    },
    "building": {
        "title": "🏰 Reglas de Building y Bases",
        "description": (
            "1. **Máximo de 4 bases por tribu en todo el cluster y 4 TPs por mapa.**\n"
            "2. Cuando un raid termina o se abandona, quita las estructuras del raid o conviértelas en base real (o avisa a un admin).\n"
            "3. Las cuevas modeadas compradas se quitan si pierdes el control de esa zona. No se reemplazan ni se reembolsan.\n"
            "4. Criaturas agresivas en wander deben estar en un Dino Leash.\n"
            "5. El spam que afecte el server hay que quitarlo si el staff lo pide.\n"
            "6. Se permite algo de structure spam (solo foundations) con medida.\n\n"
            "• **Todos los dinos sin cryo en la base deben estar en leash, máximo 5 dinos por leash.**\n\n"
            "• **Si defiendes una entrada modeada con dino, tienes que estar montado.** No bloquees ni explotes entradas modeadas con dinos.\n\n"
            "• **Los TPs no se pueden esconder dentro del render enemigo, usar para dropear en base ajena, ni colocar de forma que bypaseen cave/modded entries.**"
        )
    },
    "whiteflag": {
        "title": "🏳️ Protección White Flag",
        "description": (
            "1. El White Flag dura **7 días** y no se puede extender.\n2. Solo protege tu **base main**.\n"
            "3. Con White Flag sí puedes PvP, pero **no puedes participar en raids** hasta que se acabe (o el owner lo quite).\n"
            "4. Si rompes las reglas, pierdes la protección al momento.\n\n"
            "• **Las tribus con White Flag NO pueden poner FOBs en ninguna tribu hasta que se acabe el grace.**\n"
            "• **Ninguna tribu puede poner un FOB en tribus que estén bajo White Flag hasta que se acabe el grace.**"
        )
    },
    "pvp": {
        "title": "⚔️ Reglas de PvP / Raid",
        "description": (
            "1. Prohibido third-party raid. Solo atacantes y defensores.\n\n"
            "2. **Las alianzas pueden participar en raids/defensas si la tribu necesita igualar números.**\n"
            "*(Ejemplo: si la tribu que está siendo atacada tiene 8 jugadores activos defendiendo y tú solo tienes 4, tu alianza puede unirse para equilibrar.)*\n\n"
            "3. Los thralls solo para PvE. No para raid/defensa/PvP (tribus de 1-2 pueden pedir permiso a admin).\n"
            "4. **Raft, zeppelin, cannons no están permitidos durante raids.**\n\n"
            "5. **Spam en FOB está permitido siempre que sea para pushear a la base. Solo foundations.**\n"
            "6. Meks no meshean salvo para limpiar mesh.\n"
            "7. No donaciones a mitad de raid.\n"
            "8. Prohibido popcorn / upload / destruir o llevarse loot durante un raid.\n\n"
            "• **CS Medical Stations** y **Home Sweet Home** solo se usan para healear en **breed**. **No** se usan en raid ni para defender.\n\n"
            "• **Si countereas un FOB, tienes que tomar el control completo del raid.** Solo destruir un FOB por diversión o buscar PvP a mitad de raid **cuenta como third party.**\n\n"
            "• **Deploy masivo de dinos durante un raid al punto de afectar el performance del server no está permitido.**\n\n"
            "• **Usar carts en dinos como protección extra durante raids o defensa no está permitido.**\n\n"
            "**Reglas de FOB y Raid**\n"
            "• **Un FOB debe mantenerse activo.** Activo = soaking, destruyendo structures, matando jugadores/tames o actividad clara en el tribe log.\n"
            "• **Si un FOB no tiene actividad por 24hrs, se vuelve inactivo y puede ser Admin AOE bajo petición.**\n"
            "• **Solo 1 FOB activo por tribu por base objetivo.**\n"
            "• **Una vez que el raid termina, el FOB y todo el spam deben ser removidos en 12 hrs.** No se permiten FOBs permanentes.\n"
            "• **Si tu FOB es destruido por completo (o lo recoges / abandonas mientras estás bajo ataque), no puedes poner otro FOB ni empezar un nuevo intento de raid en esa misma base por 24 horas.**\n"
            "• **Límite diario de raid — 1 inicio de raid por tribu cada 24 horas.**\n"
            "• **No merges de tribu a mitad de raid ni miembros “temporales”.**\n"
            "• **Raidear a la misma tribu 3+ veces en 7 días sin retaliación se considera griefing** (discreción de admin + warning/wipe)."
        )
    },
    "harvest": {
        "title": "🌾 Reglas de Custom Harvest Zones",
        "description": (
            "「-✦ Custom Harvest Zones ✦-」\n\n"
            "• Prohibido buildear dentro de un rango de **30000 x 30000** de la zona.\n"
            "• TPs / FOBs sí se permiten dentro de un rango de **35000 x 35000**, pero **sin turrets**.\n"
            "• **El PvP está permitido** en estas zonas."
        )
    },
    "rathole": {
        "title": "🕳️ Reglas de Rat Holes",
        "description": (
            "• Está prohibido buildear en rat holes OP conocidos. Esto incluye spots que son extremadamente difíciles o imposibles de raidear bien (como el rat hole **Peli** y cualquier spot similar de mesh, underwater o grietas chiquitas).\n\n"
            "• Cualquier estructura que se ponga en un rat hole baneado será wipeada por el staff. Si se repite, se lleva strike.\n\n"
            "• **Si no estás seguro si tu spot es un rat hole ilegal o legal, contacta a un admin por ticket para confirmación.**"
        )
    },
    "donations": {
        "title": "💰 Reglas de Donaciones",
        "description": (
            "• **Toda venta es final.**\n• Entrega en 5–15 min. Si no llega en 30 min, abre ticket.\n"
            "• Lo comprado es para **un personaje**.\n• Prohibido revender.\n\n"
            "**Cave Edits** permanentes. Tú das la ubicación correcta. No hay move/refund. Abusarlas = se quitan + sanción.\n"
            "• Compra no da inmunidad a las reglas.\n• Chargeback = ban permanente.\n• No donaciones mid-raid."
        )
    },
    "extra": {
        "title": "📌 Reglas extra y strikes",
        "description": (
            "• Prohibido vender bases/dinos/items/tribu por dinero real.\n"
            "• Prohibido usar World Builder para trapear, esconder hitboxes o hacer unraidable.\n"
            "• Carpet turrets / spam excesivo puede ser wipeado por staff.\n\n"
            "ㆍ Warning verbal → Helena\nㆍ 1er Strike → warning escrito\nㆍ 2do Strike → restricción o ban temporal\nㆍ 3er Strike → ban largo o permanente\n\n"
            "**Grave:** RMT, dupeo, racismo, evadir ban, amenazas IRL, tirar el server.\nLa decisión del staff es final."
        )
    }
}

RULES_FR = {
    "discord": {
        "title": "💬 Règles Discord",
        "description": (
            "**1 • Inscription**\nTous les joueurs actifs doivent enregistrer leur nom in-game et le nom de leur tribu.\n\n"
            "**2 • Tolérance zéro**\nRacisme, discours de haine, discrimination, harcèlement ou toxicité ciblée sont interdits.\n"
            "1re faute → Mute • 2e → Ban 3 jours • 3e → Ban permanent.\n\n"
            "**3 • Salons**\nUtilise chaque salon pour ce qu’il sert.\n**4 • Comportement**\nLe banter compétitif est ok, pas le drama toxique.\n"
            "**5 • Contenu**\nPas de NSFW / contenu offensant.\n**6 • Coordonnées**\nInterdit de poster les coords ou screens d’une base ennemie.\n"
            "**7 • Support**\nTout passe par ticket.\n**8 • Vie privée**\nInterdit de leak des infos perso.\n"
            "**9 • Spam**\nInterdit.\n**10 • Recrutement**\nN’invite pas des gens juste pour casser le serveur.\n"
            "**11 • Staff**\nRespecte le staff. La décision du staff est finale.\n\n"
            "• **Ne pas @ les admins pour aucune situation ou tickets.**"
        )
    },
    "general": {
        "title": "📜 Règles générales du cluster",
        "description": (
            "• Pas de cheat, exploit ou mécanique non prévue.\n• Pas de mesh / build dans le mesh.\n• Pas de dupe.\n"
            "• **Pas de box raid.** Un joueur peut être boxé en 1x1, **les tames doivent pouvoir prendre des dégâts**, (pareil pour **Vehicles / Utility items / objets** — pas de structures dessus ni utilisation pour des raids).\n"
            "• Pas de tunnel sous les structures ennemies.\n• Ne laisse pas le breed sans surveillance.\n"
            "• Pas de turrets sur boats, rafts ou dinos.\n• Pas d’inside.\n• Pas de dégâts sur les structures admin.\n• Pas de raid sur les bobs.\n\n"
            "• **Un compte main par joueur.** Pas d’alts pour slots, White Flags, shop ou PvP extra."
        )
    },
    "tribe": {
        "title": "👥 Règles Tribu & Alliance",
        "description": (
            "1. Max **6 joueurs** par tribu.\n2. Une seule alliance.\n\n"
            "3. Pas de tribe/alliance cycling. **24h** d’attente minimum.\n"
            "4. Pas de changement pendant / juste avant / juste après un raid. Un délai de **24 heures** est requis après la fin d’un raid avant tout changement de tribu ou d’alliance.\n"
            "5. Le roster doit matcher le Tribe Registry.\n6. Même nom/tribu/alliance sur toutes les maps.\n"
            "7. Pas de teaming hors alliance.\n8. “Aider un pote” en PvP = teaming.\n9. Tout changement doit être update dans le registre."
        )
    },
    "building": {
        "title": "🏰 Règles Building & Bases",
        "description": (
            "1. **Maximum de 4 bases par tribu sur tout le cluster et 4 TPs par map.**\n"
            "2. Après un raid, retire les structures ou transforme-les en vraie base (ou préviens un admin).\n"
            "3. Une cave moddée achetée est retirée si tu perds la zone. Pas de remplacement.\n"
            "4. Dinos agressifs en wander = Dino Leash.\n"
            "5. Le spam qui lag le serveur doit être retiré si le staff le demande.\n"
            "6. Structure spam (foundations seulement) modéré autorisé.\n\n"
            "• **Tous les dinos non cryo à la base doivent être sous leash, max 5 dinos par leash.**\n\n"
            "• **Pour défendre une entrée moddée avec un dino, tu dois être monté dessus.** Ne bloque pas ni n’exploite les entrées moddées avec des dinos.\n\n"
            "• **Les TPs ne peuvent pas être cachés dans le render ennemi, utilisés pour drop dans une base, ou placés pour bypasser cave/modded entries.**"
        )
    },
    "whiteflag": {
        "title": "🏳️ Protection White Flag",
        "description": (
            "1. White Flag = **7 jours**, non prolongeable.\n2. Protège uniquement ta **base main**.\n"
            "3. PvP autorisé, mais **pas de participation aux raids** tant que le flag est actif.\n"
            "4. Enfreindre les règles = perte immédiate de la protection.\n\n"
            "• **Les tribus sous White Flag ne peuvent PAS placer de FOBs sur aucune tribu avant la fin du grace.**\n"
            "• **Aucune tribu ne peut placer un FOB sur une tribu sous White Flag avant la fin du grace.**"
        )
    },
    "pvp": {
        "title": "⚔️ Règles PvP / Raid",
        "description": (
            "1. Pas de third-party raid. Seulement les tribus/alliances attaquantes et défendantes.\n\n"
            "2. **Les alliances peuvent participer aux raids/défenses si la tribu a besoin d’égaliser les nombres.**\n"
            "*(Exemple : si la tribu attaquée a 8 joueurs actifs en défense et que vous n’en avez que 4, votre alliance peut rejoindre pour équilibrer.)*\n\n"
            "3. Thralls = PvE seulement.\n4. **Raft, zeppelin, cannons ne sont pas autorisés pendant les raids.**\n\n"
            "5. **Spam au FOB autorisé tant que c’est pour push vers la base. Foundations seulement.**\n"
            "6. Mek : pas de mesh sauf pour clear du mesh.\n"
            "7. Pas de donations mid-raid.\n"
            "8. Pas de popcorn / upload / destruction ou vol de loot pendant un raid.\n\n"
            "• **CS Medical Stations** et **Home Sweet Home** = heal de **breed** uniquement, pas en raid/défense.\n\n"
            "• **Si tu counter un FOB, tu dois prendre le contrôle complet du raid.** Détruire un FOB juste pour le fun ou chercher du PvP en plein raid **compte comme third party.**\n\n"
            "• **Déploiement massif de dinos pendant un raid au point d’affecter les performances du serveur n’est pas autorisé.**\n\n"
            "• **Utiliser des carts sur des dinos comme protection extra pendant les raids ou la défense n’est pas autorisé.**\n\n"
            "**Règles FOB & Raid**\n"
            "• **Un FOB doit rester actif.** Actif = soaking, destruction de structures, kills joueurs/tames ou activité claire dans le tribe log.\n"
            "• **Si un FOB n’a aucune activité pendant 24h, il devient inactif et peut être Admin AOE sur demande.**\n"
            "• **Seulement 1 FOB actif par tribu par base cible.**\n"
            "• **Une fois le raid terminé, le FOB et tout le spam doivent être retirés dans les 12h.** Les FOBs permanents ne sont pas autorisés.\n"
            "• **Si votre FOB est entièrement détruit (ou que vous le ramassez / abandonnez pendant l’attaque), vous ne pouvez pas poser un autre FOB ni commencer une nouvelle tentative de raid sur cette même base pendant 24h.**\n"
            "• **Limite quotidienne de raid — 1 début de raid par tribu toutes les 24h.**\n"
            "• **Pas de merges de tribu en plein raid ni de membres “temporaires”.**\n"
            "• **Raider la même tribu 3+ fois en 7 jours sans rétorsion est considéré comme du griefing** (discrétion admin + warning/wipe)."
        )
    },
    "harvest": {
        "title": "🌾 Règles Custom Harvest Zones",
        "description": (
            "「-✦ Custom Harvest Zones ✦-」\n\n"
            "• Aucun building dans une zone de **30000 x 30000** autour de la harvest zone.\n"
            "• TPs / FOBs autorisés dans une zone de **35000 x 35000**, mais **aucune turret**.\n"
            "• **Le PvP est autorisé** dans ces zones."
        )
    },
    "rathole": {
        "title": "🕳️ Règles Rat Hole",
        "description": (
            "• Il est interdit de build dans les rat holes OP connus. Ça inclut les spots qui sont extrêmement durs ou impossibles à raid correctement (comme le rat hole **Peli** et tout spot similaire en mesh, underwater ou petites crevasses).\n\n"
            "• Toute structure placée dans un rat hole banni sera wipe par le staff. Les récidivistes prennent un strike.\n\n"
            "• **Si tu n’es pas sûr que ton spot est un rat hole illégal ou légal, contacte un admin par ticket pour confirmation.**"
        )
    },
    "donations": {
        "title": "💰 Règles Donations",
        "description": (
            "• Toute vente est finale.\n• Livraison 5–15 min. Ticket si rien en 30 min.\n• Un seul personnage.\n• Pas de revente.\n"
            "• Cave edits permanentes, pas de refund/move.\n• Un achat ne donne aucune immunité.\n• Chargeback = ban permanent.\n• Pas de donation mid-raid."
        )
    },
    "extra": {
        "title": "📌 Règles extra & strikes",
        "description": (
            "• Interdit de vendre bases/dinos/items/tribu pour de l’argent réel.\n"
            "• World Builder : pas de trap, hitbox cachée ou géométrie unraidable.\n"
            "• Carpet turrets / spam excessif = wipe staff possible.\n\n"
            "Warning verbal → Helena • 1er strike → warning écrit • 2e → restriction/ban tempo • 3e → long ban / perma.\nDécision du staff finale."
        )
    },
}

RULES_DE = {
    "discord": {
        "title": "💬 Discord-Regeln",
        "description": (
            "**1 • Registrierung**\nJeder aktive Spieler muss Ingame-Name und Tribe-Name im Register-Channel angeben.\n\n"
            "**2 • Null Toleranz**\nRassismus, Hassrede, Diskriminierung, Belästigung oder gezielte Toxizität sind verboten.\n"
            "1. Verstoß → Mute • 2. → 3-Tage-Ban • 3. → Permanenter Ban.\n\n"
            "**3 • Channels**\nNutze Channels nur für ihren Zweck.\n**4 • Verhalten**\nCompetitives Banter ist ok, toxisches Drama nicht.\n"
            "**5 • Content**\nKein NSFW / anstößiger Content.\n**6 • Koordinaten**\nKeine Base-Coords oder Screenshots fremder Bases öffentlich posten.\n"
            "**7 • Support**\nAlles über Tickets.\n**8 • Privatsphäre**\nKeine persönlichen Daten leaken.\n"
            "**9 • Spam**\nVerboten.\n**10 • Recruiting**\nKeine Leute einladen, deren Ziel nur Drama/Schaden ist.\n"
            "**11 • Staff**\nRespektiert den Staff. Staff-Entscheidung ist final.\n\n"
            "• **Keine Admins @ für irgendeine Situation oder Tickets.**"
        )
    },
    "general": {
        "title": "📜 Allgemeine Cluster-Regeln",
        "description": (
            "• Kein Cheaten, Exploiten oder unbeabsichtigte Mechanics.\n• Kein Meshen / Bauen im Mesh.\n• Kein Dupen.\n"
            "• **Kein Box-Raid.** Spieler dürfen 1x1 geboxt werden, **Tames müssen damagebar bleiben**, (gilt auch für **Vehicles / Utility Items / Objekte** — keine Structures drauf und nicht für Raids nutzen).\n"
            "• Kein Tunneln unter gegnerischen Structures.\n• Breeding nicht unbeaufsichtigt lassen.\n"
            "• Keine Turrets auf Boats, Rafts oder Dinos.\n• Kein Insiden.\n• Keine Admin-Structures zerstören.\n• Kein Bob-Raiden.\n\n"
            "• **Ein Main-Account pro Spieler.** Keine Alts für extra Slots, White Flags, Shop oder PvP."
        )
    },
    "tribe": {
        "title": "👥 Tribe- & Alliance-Regeln",
        "description": (
            "1. Max **6 Spieler** pro Tribe.\n2. Nur **eine Alliance**.\n\n"
            "3. Kein Tribe-/Alliance-Cycling. Mindestens **24 Stunden** warten.\n"
            "4. Kein Wechsel während / direkt vor / direkt nach einem Raid. Eine Wartezeit von **24 Stunden** nach Ende eines Raids ist erforderlich, bevor ein Tribe- oder Alliance-Wechsel möglich ist.\n"
            "5. Roster muss zum Tribe Registry passen.\n6. Gleicher Tribe-/Alliance-Name auf allen Maps.\n"
            "7. Kein Teaming außerhalb der Alliance.\n8. „Nur einem Bro helfen“ im PvP = Teaming.\n9. Änderungen müssen im Register geupdatet werden."
        )
    },
    "building": {
        "title": "🏰 Building- & Base-Regeln",
        "description": (
            "1. **Maximum von 4 Bases pro Tribe über den gesamten Cluster und 4 TPs pro Map.**\n"
            "2. Nach einem Raid Raid-Structures entfernen oder in eine echte Base umwandeln (oder Admin Bescheid geben).\n"
            "3. Gekaufte Mod-Caves werden entfernt, wenn du die Zone verlierst. Kein Replace/Refund.\n"
            "4. Aggressive Wander-Dinos müssen im Dino Leash sein.\n"
            "5. Performance-Spam muss auf Staff-Anweisung weg.\n"
            "6. Structure Spam (nur Foundations) in moderatem Umfang erlaubt.\n\n"
            "• **Alle uncryo’ten Dinos an der Base müssen unter Leash sein, max 5 Dinos pro Leash.**\n\n"
            "• **Wenn du eine modded Entry mit einem Dino verteidigst, musst du drauf sitzen.** Blockiere oder explote modded Entries nicht mit Dinos.\n\n"
            "• **TPs dürfen nicht im Enemy-Render versteckt, zum Droppen in fremde Bases oder zum Bypassen von Cave/Modded Entries genutzt werden.**"
        )
    },
    "whiteflag": {
        "title": "🏳️ White-Flag-Schutz",
        "description": (
            "1. White Flag gilt **7 Tage** und kann nicht verlängert werden.\n2. Schützt nur die **Main Base**.\n"
            "3. PvP ist erlaubt, aber **keine Raid-Teilnahme**, solange der Flag aktiv ist.\n"
            "4. Regelbruch = sofortiger Verlust des Schutzes.\n\n"
            "• **Tribes unter White Flag dürfen KEINE FOBs auf irgendeinen Tribe setzen, bis der Grace vorbei ist.**\n"
            "• **Kein Tribe darf ein FOB auf Tribes unter White Flag setzen, bis der Grace vorbei ist.**"
        )
    },
    "pvp": {
        "title": "⚔️ PvP- / Raid-Regeln",
        "description": (
            "1. Kein Third-Party-Raid. Nur angreifende und verteidigende Tribes/Alliances.\n\n"
            "2. **Alliances dürfen an Raids/Defenses teilnehmen, wenn der Tribe die Zahlen ausgleichen muss.**\n"
            "*(Beispiel: Wenn der angegriffene Tribe 8 aktive Spieler in der Defense hat und ihr nur 4 habt, darf eure Alliance beitreten, um auszugleichen.)*\n\n"
            "3. Thralls nur PvE.\n4. **Raft, Zeppelin, Cannons sind während Raids nicht erlaubt.**\n\n"
            "5. **Spam am FOB ist erlaubt, solange es zum Pushen zur Base dient. Nur Foundations.**\n"
            "6. Meks dürfen nicht meshen, außer zum Clearen von Mesh.\n"
            "7. Keine Donations mitten im Raid.\n"
            "8. Kein Popcorn / Upload / Loot zerstören oder mitnehmen während eines Raids.\n\n"
            "• **CS Medical Stations** und **Home Sweet Home** nur zum Healen beim **Breed**, nicht im Raid/Defense.\n\n"
            "• **Wenn du ein FOB counterst, musst du die volle Kontrolle über den Raid übernehmen.** Ein FOB nur zum Spaß zerstören oder mid-raid PvP suchen **zählt als Third Party.**\n\n"
            "• **Massen-Dino-Deployment während eines Raids, das die Server-Performance beeinträchtigt, ist nicht erlaubt.**\n\n"
            "• **Carts auf Dinos als extra Schutz während Raids oder Defense zu nutzen ist nicht erlaubt.**\n\n"
            "**FOB- & Raid-Regeln**\n"
            "• **Ein FOB muss aktiv bleiben.** Aktiv = Soaking, Structures zerstören, Spieler/Tames killen oder klare Tribe-Log-Aktivität.\n"
            "• **Wenn ein FOB 24h keine Aktivität hat, wird es inaktiv und kann auf Anfrage Admin AOE werden.**\n"
            "• **Nur 1 aktiver FOB pro Tribe pro Ziel-Base.**\n"
            "• **Sobald ein Raid endet, müssen der FOB und der gesamte Spam innerhalb von 12h entfernt werden.** Permanente FOBs sind nicht erlaubt.\n"
            "• **Wenn dein FOB vollständig zerstört wird (oder du ihn aufnimmst / aufgibst, während du unter Angriff bist), darfst du keinen neuen FOB platzieren oder einen neuen Raid-Versuch auf dieselbe Base für 24 Stunden starten.**\n"
            "• **Tägliches Raid-Limit — 1 Raid-Start pro Tribe alle 24 Stunden.**\n"
            "• **Keine Tribe-Merges mitten im Raid oder „temporäre“ Mitglieder.**\n"
            "• **Die gleiche Tribe 3+ Mal in 7 Tagen ohne Retaliation zu raiden gilt als Griefing** (Admin-Ermessen + Warning/Wipe)."
        )
    },
    "harvest": {
        "title": "🌾 Custom-Harvest-Zone-Regeln",
        "description": (
            "「-✦ Custom Harvest Zones ✦-」\n\n"
            "• Kein Building innerhalb von **30000 x 30000** um die Harvest Zone.\n"
            "• TPs / FOBs sind innerhalb von **35000 x 35000** erlaubt, aber **keine Turrets**.\n"
            "• **PvP ist in diesen Zonen erlaubt.**"
        )
    },
    "rathole": {
        "title": "🕳️ Rat-Hole-Regeln",
        "description": (
            "• Bauen in bekannten OP Rat Holes ist verboten. Das schließt Spots ein, die extrem schwer oder unmöglich richtig zu raiden sind (wie der **Peli** Rat Hole und ähnliche Mesh-/Underwater-/kleine Spalten-Spots).\n\n"
            "• Alle Structures in einem gebannten Rat Hole werden vom Staff gewiped. Wiederholungstäter bekommen einen Strike.\n\n"
            "• **Wenn du unsicher bist, ob dein Spot ein illegales oder legales Rat Hole ist, kontaktiere einen Admin per Ticket zur Bestätigung.**"
        )
    },
    "donations": {
        "title": "💰 Donations-Regeln",
        "description": (
            "• Alle Käufe sind final.\n• Lieferung 5–15 Min. Ticket nach 30 Min.\n• Nur für einen Character.\n• Kein Weiterverkauf.\n"
            "• Cave Edits sind permanent, kein Move/Refund.\n• Kaufen gibt keine Regel-Immunität.\n• Chargeback = Permaban.\n• Keine Donation mid-raid."
        )
    },
    "extra": {
        "title": "📌 Extra-Regeln & Strikes",
        "description": (
            "• Kein Verkauf von Bases/Dinos/Items/Tribe für Echtgeld.\n"
            "• World Builder nicht für Traps, versteckte Hitboxes oder unraidable Geometry.\n"
            "• Zu viele Carpet-Turrets / Spam kann der Staff wipen.\n\n"
            "Verbal Warning → Helena • 1. Strike → schriftliche Warnung • 2. Strike → Restriction/Tempban • 3. Strike → Long Ban/Perm.\nStaff-Entscheidung ist final."
        )
    },
}

RULE_OPTIONS_EN = [
    discord.SelectOption(label="Discord Rules", value="discord", emoji="💬"),
    discord.SelectOption(label="General Rules", value="general", emoji="📜"),
    discord.SelectOption(label="Tribe & Alliance", value="tribe", emoji="👥"),
    discord.SelectOption(label="Building & Base", value="building", emoji="🏰"),
    discord.SelectOption(label="White Flag", value="whiteflag", emoji="🏳️"),
    discord.SelectOption(label="PvP / Raid Rules", value="pvp", emoji="⚔️"),
    discord.SelectOption(label="Harvest Zones", value="harvest", emoji="🌾"),
    discord.SelectOption(label="Rat Hole Rules", value="rathole", emoji="🕳️"),
    discord.SelectOption(label="Donations Rules", value="donations", emoji="💰"),
    discord.SelectOption(label="Extra + Strikes", value="extra", emoji="📌"),
]

# Spanish, French, German select options (same structure, translated labels)
RULE_OPTIONS_ES = [
    discord.SelectOption(label="Reglas de Discord", value="discord", emoji="💬"),
    discord.SelectOption(label="Reglas generales", value="general", emoji="📜"),
    discord.SelectOption(label="Tribu y Alianza", value="tribe", emoji="👥"),
    discord.SelectOption(label="Building y Bases", value="building", emoji="🏰"),
    discord.SelectOption(label="White Flag", value="whiteflag", emoji="🏳️"),
    discord.SelectOption(label="PvP / Raid", value="pvp", emoji="⚔️"),
    discord.SelectOption(label="Harvest Zones", value="harvest", emoji="🌾"),
    discord.SelectOption(label="Reglas de Rat Holes", value="rathole", emoji="🕳️"),
    discord.SelectOption(label="Donaciones", value="donations", emoji="💰"),
    discord.SelectOption(label="Extra + Strikes", value="extra", emoji="📌"),
]

RULE_OPTIONS_FR = [
    discord.SelectOption(label="Règles Discord", value="discord", emoji="💬"),
    discord.SelectOption(label="Règles générales", value="general", emoji="📜"),
    discord.SelectOption(label="Tribu & Alliance", value="tribe", emoji="👥"),
    discord.SelectOption(label="Building & Bases", value="building", emoji="🏰"),
    discord.SelectOption(label="White Flag", value="whiteflag", emoji="🏳️"),
    discord.SelectOption(label="PvP / Raid", value="pvp", emoji="⚔️"),
    discord.SelectOption(label="Harvest Zones", value="harvest", emoji="🌾"),
    discord.SelectOption(label="Règles Rat Hole", value="rathole", emoji="🕳️"),
    discord.SelectOption(label="Donations", value="donations", emoji="💰"),
    discord.SelectOption(label="Extra + Strikes", value="extra", emoji="📌"),
]

RULE_OPTIONS_DE = [
    discord.SelectOption(label="Discord-Regeln", value="discord", emoji="💬"),
    discord.SelectOption(label="Allgemeine Regeln", value="general", emoji="📜"),
    discord.SelectOption(label="Tribe & Alliance", value="tribe", emoji="👥"),
    discord.SelectOption(label="Building & Bases", value="building", emoji="🏰"),
    discord.SelectOption(label="White Flag", value="whiteflag", emoji="🏳️"),
    discord.SelectOption(label="PvP / Raid", value="pvp", emoji="⚔️"),
    discord.SelectOption(label="Harvest Zones", value="harvest", emoji="🌾"),
    discord.SelectOption(label="Rat-Hole-Regeln", value="rathole", emoji="🕳️"),
    discord.SelectOption(label="Donations", value="donations", emoji="💰"),
    discord.SelectOption(label="Extra + Strikes", value="extra", emoji="📌"),
]


def make_select(data, custom_id, placeholder, footer, options):
    class DynSelect(discord.ui.Select):
        def __init__(self):
            super().__init__(placeholder=placeholder, options=options, custom_id=custom_id)

        async def callback(self, interaction: discord.Interaction):
            item = data[self.values[0]]
            embed = discord.Embed(title=item["title"], description=item["description"], color=GLACIAL_COLOR)
            embed.set_footer(text=footer)
            await interaction.response.send_message(embed=embed, ephemeral=True)
    return DynSelect


InfoSelect = make_select(INFO, "glacial_info_select", "Choose a category...", "GA50X Cluster Info Bot", [
    discord.SelectOption(label="Custom Drops", value="custom_drops", emoji="📦"),
    discord.SelectOption(label="Orbital Drops", value="orbital_drops", emoji="🛰️"),
    discord.SelectOption(label="Modded Crafts", value="modded_crafts", emoji="🛠️"),
    discord.SelectOption(label="Bosses", value="bosses", emoji="🦖"),
    discord.SelectOption(label="Mods List", value="mods", emoji="📜"),
    discord.SelectOption(label="Player & Dino Stats", value="stats", emoji="📊"),
    discord.SelectOption(label="Nerfed & Banned Dinos", value="nerfed_banned", emoji="🚫"),
])
RulesSelect = make_select(RULES, "glacial_rules_select", "Choose a rules category...", "GA50X • Rules", RULE_OPTIONS_EN)
RulesEsSelect = make_select(RULES_ES, "glacial_rules_es_select", "Elige una categoría...", "GA50X • Reglas", RULE_OPTIONS_ES)
RulesFrSelect = make_select(RULES_FR, "glacial_rules_fr_select", "Choisis une catégorie...", "GA50X • Règles", RULE_OPTIONS_FR)
RulesDeSelect = make_select(RULES_DE, "glacial_rules_de_select", "Kategorie wählen...", "GA50X • Regeln", RULE_OPTIONS_DE)


class InfoView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(InfoSelect())


class RulesView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(RulesSelect())


class RulesEsView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(RulesEsSelect())


class RulesFrView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(RulesFrSelect())


class RulesDeView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(RulesDeSelect())


intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    bot.add_view(InfoView())
    bot.add_view(RulesView())
    bot.add_view(RulesEsView())
    bot.add_view(RulesFrView())
    bot.add_view(RulesDeView())
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
        title="❄️ GA50X CLUSTER INFO",
        description="Click the dropdown below to view server information.",
        color=GLACIAL_COLOR
    )
    await interaction.response.send_message(embed=embed, view=InfoView())


@bot.tree.command(name="rules", description="Post the rules panel (English)")
@app_commands.checks.has_permissions(administrator=True)
async def rules(interaction: discord.Interaction):
    embed = discord.Embed(title="❄️ GA50X RULES", description="Choose a category below.", color=GLACIAL_COLOR)
    await interaction.response.send_message(embed=embed, view=RulesView())


@bot.tree.command(name="rules_es", description="Publicar el panel de reglas en Español")
@app_commands.checks.has_permissions(administrator=True)
async def rules_es(interaction: discord.Interaction):
    embed = discord.Embed(title="❄️ GA50X REGLAS", description="Elige una categoría abajo.", color=GLACIAL_COLOR)
    await interaction.response.send_message(embed=embed, view=RulesEsView())


@bot.tree.command(name="rules_fr", description="Publier le panneau des règles en Français")
@app_commands.checks.has_permissions(administrator=True)
async def rules_fr(interaction: discord.Interaction):
    embed = discord.Embed(title="❄️ GA50X RÈGLES", description="Choisis une catégorie ci-dessous.", color=GLACIAL_COLOR)
    await interaction.response.send_message(embed=embed, view=RulesFrView())


@bot.tree.command(name="rules_de", description="Regeln-Panel auf Deutsch posten")
@app_commands.checks.has_permissions(administrator=True)
async def rules_de(interaction: discord.Interaction):
    embed = discord.Embed(title="❄️ GA50X REGELN", description="Wähle unten eine Kategorie.", color=GLACIAL_COLOR)
    await interaction.response.send_message(embed=embed, view=RulesDeView())


@setup_panel.error
@rules.error
@rules_es.error
@rules_fr.error
@rules_de.error
async def permission_error(interaction: discord.Interaction, error):
    if isinstance(error, app_commands.MissingPermissions):
        await interaction.response.send_message("You need Administrator permission.", ephemeral=True)


bot.run(TOKEN)
