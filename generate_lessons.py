import os

def generate_lessons():
    lessons_data = [
        {
            "id": "001",
            "title": "Média a aktuality",
            "heb_title": "מדיה וחדשות",
            "article": "הבוקר פורסם כי הממשלה החליטה להשקיע משאבים נוספים בשיפור התשתיות. השר הממונה ציין כי המהלך נועד לחזק את הכלכלה ולספק מקומות עבודה חדשים לתושבים.",
            "vocab": [
                ("לפרסם", "פ.ר.ס.ם", "lefarsem", "publikovat / zveřejnit", "פורסם כי הממשלה החליטה"),
                ("ממשלה", "מ.ש.ל", "memšala", "vláda", "הממשלה החליטה להשקיע"),
                ("להשקיע", "ש.ק.ע", "lehaškia", "investovat", "להשקיע משאבים נוספים"),
                ("משאבים", "ש.א.ב", "mašavim", "zdroje", "משאבים כלכליים"),
                ("תשתית", "ש.ת.ת", "taštit", "infrastruktura", "שיפור התשתיות"),
                ("ממונה", "מ.נ.ה", "memune", "pověřený / odpovědný", "השר הממונה על הפרויקט"),
                ("מהלך", "ה.ל.ך", "mahalach", "krok / proces / tah", "המהלך נועד לחזק"),
                ("נועד", "י.ע.ד", "no'ad", "určen k / má za cíl", "הפרויקט נועד לתושבים"),
                ("כלכלה", "כ.ל.כ.ל", "kalkala", "ekonomika", "הכלכלה המקומית חזקה"),
                ("תושב", "י.ש.ב", "tošav", "obyvatel", "התושבים גרים בצפון")
            ],
            "grammar": [
                "V textu vidíme pasivum <strong>פורסם</strong> (pursam) od slovesa <em>lefarsem</em>. V moderní hebrejštině se pasivum v médiích používá velmi často k vyjádření objektivity.",
                "Vazba <strong>נועד ל-</strong> (no'ad le-) se používá pro vyjádření účelu nebo určení (např. <em>Tato kniha je určena pro děti</em> – הספר הזה נועד לילדים)."
            ],
            "exercises": [
                ("הבוקר _______ כי הממשלה החליטה להשקיע.", "פורסם"),
                ("המהלך _______ לחזק את הכלכלה.", "נועד"),
                ("השר ה_______ על הפרויקט ציין את חשיבותו.", "ממונה")
            ],
            "topic": "média"
        },
        {
            "id": "002",
            "title": "Technologie a high-tech",
            "heb_title": "טכנולוגיה והיי-טק",
            "article": "ישראל ידועה בעולם כ\"אומת הסטארט-אפ\". חברות ישראליות רבות מפתחות טכנולוגיה חדשנית בתחומי הבינה המלאכותית והסייבר. כל חברה מנסה למצוא פתרון לבעיה גלובלית וליצור מוצר מוצלח שישרת מיליוני משתמשים ברחבי העולם.",
            "vocab": [
                ("לפתח", "פ.ת.ח", "lefateach", "vyvíjet / rozvíjet", "לפתח טכנולוגיה חדשה"),
                ("חדשני", "ח.ד.ש", "chadašani", "inovativní", "מוצר חדשני ומעניין"),
                ("תחום", "ת.ח.מ", "tchum", "obor / oblast", "בתחום הבינה המלאכותית"),
                ("בינה מלאכותית", "---", "bina melachutit", "umělá inteליgence", "עתיד הבינה המלאכותית"),
                ("חברה", "ח.ב.ר", "chevra", "společnost / firma", "חברת סטארט-אפ"),
                ("פתרון", "פ.ת.ר", "pitron", "řeשení", "למצוא פתרון לבעיה"),
                ("מוצר", "י.צ.ר", "mucar", "produkt / výrobek", "מוצר מוצלח מאוד"),
                ("משתמש", "ש.מ.ש", "mištameš", "uživatel", "מיליוני משתמשים בעולם"),
                ("פיתוח", "פ.ת.ח", "pituach", "vývoj", "מרכז פיתוח גדול"),
                ("מוצלח", "צ.ל.ח", "muclach", "úspěשný", "פרויקט מוצלח ורווחי")
            ],
            "grammar": [
                "Slovo <strong>פיתוח</strong> (pituach) – je podstatné jméno slovesné od slovesa <strong>לפתח</strong> (lefateach). Tento vzor (ki-tu-ach) je pro kmen Pi'el velmi typický.",
                "U složenin jako <strong>בינה מלאכותית</strong> (bina melachutit) musí přídavné jméno souhlasit v rodě (obě jsou v ženském rodě)."
            ],
            "exercises": [
                ("ישראל מפתחת טכנולוגיה _______.", "חדשנית"),
                ("החברה מנסה למצוא _______ לבעיה.", "פתרון"),
                ("יש מיליוני _______ ברחבי העולם.", "משתמשים")
            ],
            "topic": "technologie"
        },
        {
            "id": "003",
            "title": "Práce a kariéra",
            "heb_title": "עבודה וקריירה",
            "article": "חיפוש עבודה בישראל דורש הכנה קפדנית. המועמד צריך לשלוח קורות חיים (קו\"ח) מעודכנים ולהתכונן לראיון עבודה. במהלך הראיון, המעסיק בודק את הניסיון המקצועי של המועמד ואת היכולת שלו להשתלב בצוות. אם הראיון מוצלח, הצדדים חותמים על חוזה עבודה.",
            "vocab": [
                ("ראיון", "ר.א.ה", "reajon", "pohovor", "ראיון עבודה"),
                ("משרה", "ש.ר.ה", "misra", "pracovní pozice", "משרה מלאה"),
                ("ניסיון", "נ.ס.ה", "nisajon", "zkuשenost", "יש לי ניסיון"),
                ("מעסיק", "ע.ס.ק", "ma'asik", "zaměstnavatel", "המעסיק שלי נחמד"),
                ("להתפטר", "פ.ט.ר", "lehitpater", "dát výpověď", "החלטתי להתפטר"),
                ("משכורת", "ש.כ.ר", "maschoret", "plat / mzda", "משכורת גבוהה"),
                ("חוזה", "ח.ז.ה", "choze", "smlouva", "חתמנו על חוזה"),
                ("הטבות", "ט.ו.ב", "hatavot", "benefity", "הטבות סוציאליות"),
                ("לקדם", "ק.ד.ם", "lekadem", "povýשit / propagovat", "הבוס רוצה לקדם אותי"),
                ("קו\"ח", "ח.י.ה", "korot chajim", "životopis", "שלחתי קו\"ח")
            ],
            "grammar": [
                "Kořen <strong>ש.כ.ר</strong> (S-K-R) souvisí s odměnou. Najdeme ho ve slovech <em>sechar</em> (mzda) nebo <em>ליsckor</em> (najmout si).",
                "Slovo <strong>ראיון</strong> (reajon – pohovor) má kořen <strong>ר.א.ה</strong> (R-A-H), což je kořen pro „vidět“ (ליrot). Pohovor je tedy vlastně „vzájemné prohlédnutí“."
            ],
            "exercises": [
                ("שלחתי _______ מעודכנים למעסיק.", "קו\"ח"),
                ("הצדדים חתמו על _______ עבודה.", "חוזה"),
                ("אני רוצה לקבל _______ גבוהה יותר.", "משכורת")
            ],
            "topic": "práce"
        },
        {
            "id": "004",
            "title": "Psychologie a emoce",
            "heb_title": "פסיכולוגיה ורגשות",
            "article": "הבריאות הנפשית חשובה לא פחות מהבריאות הפיזית. אנשים רבים סובלים מתחושת חרדה או דיכאון בגלל הלחץ המודרני. המודעות לחשיבות הטיפול הפסיכולוגi עלתה בשנים האחרונות. פיתוח ביטחון עצמי ומציאת מקורות של אושר פנימי יכולים לשפר את איכות החיים.",
            "vocab": [
                ("רגש", "ר.ג.ש", "regeš", "emoce / cit", "רגש חזק"),
                ("תחושה", "ח.ו.ש", "tchuša", "pocit / vjem", "תחושה של חופש"),
                ("דיכאון", "ד.כ.א", "dikaon", "deprese", "הוא סובל מדיכאון"),
                ("חרדה", "ח.ר.ד", "charada", "úzkost", "התקף חרדה"),
                ("מודעות", "י.ד.ע", "muda'ut", "povědomí", "מודעות עצמית"),
                ("ביטחון", "ב.ט.ח", "bitachon", "bezpečí / sebevědomí", "ביטחון עצמי"),
                ("אושר", "א.ש.ר", "ošer", "שtěstí", "אושר אמיתי"),
                ("סבל", "ס.ב.ל", "sevel", "utrpení", "סבל פיזי"),
                ("זיכרון", "ז.כ.ר", "zikaron", "paměť / vzpomínka", "זיכרון לטווח ארוך"),
                ("השפעה", "ש.פ.ע", "hašpa'a", "vליv / dopad", "השפעה חיובית")
            ],
            "grammar": [
                "Přípona <strong>-on</strong> se v hebrejštině často používá pro stavy, nemoci nebo abstraktní pojmy (např. <em>zikaron</em> – paměť, <em>ra'avon</em> – hlad).",
                "Podstatné jméno <strong>תחושה</strong> (tchuša) má kořen <strong>ח.ו.ש</strong> (Ch-W-Š), ze kterého pochází i sloveso <em>lahuש</em> (cítit)."
            ],
            "exercises": [
                ("הוא סובל מתחושת _______ בגלל הלחץ.", "חרדה"),
                ("פיתוח _______ עצמי הוא חשוב.", "ביטחון"),
                ("החוויה הזאת השאירה אצלי _______ חזק.", "רגש")
            ],
            "topic": "psychologie"
        },
        {
            "id": "005",
            "title": "Právo a společnost",
            "heb_title": "משפט וחברה",
            "article": "החוק במדינת ישראל מבטיח שוויון זכויות לכל האזרחים. כאשר אדם עובר על החוק, המשטרה חוקרת את המקרה והתובע מגיש כתב אישום לבית המשפט. בסיום התהליך, השופט נותן פסק דין הקובע אם הנאשם אשם או זכאי.",
            "vocab": [
                ("חוק", "ח.ק.ק", "chok", "zákon", "לשמור על החוק"),
                ("זכות", "ז.כ.ה", "zchut", "právo (nárok)", "זכות הדיבור"),
                ("חובה", "ח.ו.ב", "chova", "povinnost", "חובות האזרח"),
                ("שופט", "ש.פ.ט", "šofet", "soudce", "השופט נתן פסק דין"),
                ("עורך דין", "ע.ר.ך", "orech din", "advokát / právník", "עורך דין פלילי"),
                ("אשם", "א.ש.ם", "ašam", "vinný", "הוא נמצא אשם"),
                ("עדות", "ע.ו.ד", "edut", "svědectví", "עדות בבית המשפט"),
                ("ראיה", "ר.א.ה", "reaja", "důkaz", "יש ראיות חזקות"),
                ("צדק", "צ.ד.ק", "cedek", "spravedlnost", "מערכת הצדק"),
                ("זכאי", "ז.כ.ה", "zakai", "nevinný / oprávněný", "הנאשם נמצא זכאי")
            ],
            "grammar": [
                "V právní hebrejštině se často používá vazba <strong>smichut</strong>. Například <strong>בית משפט</strong> (Beit Miשpat – Soud). Člen <em>ha-</em> se dává až před druhé slovo.",
                "Slovo <strong>פסק דין</strong> (psek din) znamená rozsudek, doslova „řez soudu“."
            ],
            "exercises": [
                ("הוא פנה ל_______ כדי לקבל ייצוג.", "עורך דין"),
                ("ה_______ נתן פסק דין בסיום המשפט.", "שופט"),
                ("לכל אזרח יש _______ וחובות.", "זכויות")
            ],
            "topic": "právo"
        },
        {
            "id": "006",
            "title": "Kultura a volný čas",
            "heb_title": "תרבות ופנאי",
            "article": "התרבות הישראלית עשירה ביצירתיות ובהשראה. בכל שנה מתקיימים פסטיבלים של מוזיקה, תיאטרון ואמנות ברחבי הארץ. תערוכה חדשה שנפתחה במוזיאון מציגה יצירות של אמנים צעירים המבטאים את הכישרון שלהם.",
            "vocab": [
                ("אמנות", "א.מ.ן", "amanut", "umění", "אמנות מודרנית"),
                ("יצירה", "י.צ.ר", "jecira", "dílo / tvorba", "יצירת מופת"),
                ("הופעה", "י.פ.ע", "hofa'a", "představení", "הופעה חיה"),
                ("תערוכה", "ע.ר.ך", "ta'arucha", "výstava", "תערוכה במוזיאון"),
                ("השראה", "ש.ר.ה", "hašra'a", "inspirace", "קיבלתי השראה"),
                ("כישרון", "כ.ש.ר", "kišaron", "talent", "כישרון מוזיקלי"),
                ("קהל", "ק.ה.ל", "kahal", "pubליka / dav", "קהל גדול"),
                ("ביקורת", "ב.ק.ר", "bikoret", "kritika / recenze", "ביקורת חיובית"),
                ("סגנון", "ס.ג.נ", "signon", "styl", "סגנון אישי"),
                ("בילוי", "ב.ל.ה", "biluj", "zábava / trávení času", "בילוי עם חברים")
            ],
            "grammar": [
                "Sloveso <strong>לבלות</strong> (levalot – bavit se) tvoří podstatné jméno <strong>בילוי</strong> (biluj) podle vzoru kmenu Pi'el (ki-tu-y).",
                "Slovo <strong>אמנות</strong> (amanut – umění) pochází z kořene <strong>א.מ.ן</strong>, který souvisí s vírou a pravdou (amen)."
            ],
            "exercises": [
                ("האמן הציג את ה_______ החדשה שלו.", "יצירה"),
                ("ה_______ מחא כפיים בסיום ההופעה.", "קהל"),
                ("הייתה _______ טובה על הסרט בעיתון.", "ביקורת")
            ],
            "topic": "kultura"
        },
        {
            "id": "007",
            "title": "Slang a idiomy",
            "heb_title": "סלנג וביטויים",
            "article": "למרות שהעברית הרשמית יפה מאוד, ביומיום הישראלים משתמשים בסלנג רב. אם מישהו אומר לכם \"חבל על הזמן\", הוא בדרך כלל מתכוון שמשהו היה מצוין. המילה \"תכלס\" עוזרת לנו להגיע לעיקר השיחה. כשקורה משהו מביך, אנחנו קוראים לזה \"פדיחה\".",
            "vocab": [
                ("סבבה", "---", "sababa", "v pohodě / ok", "הכל סבבה"),
                ("פדיחה", "---", "fadicha", "trapas / ostuda", "הייתה לי פדיחה"),
                ("אשכרה", "---", "aשkara", "fakt / vážně", "הוא אשכרה אמר את זה"),
                ("תכלס", "---", "tachles", "vlastně / k věci", "תכלס, אתה צודק"),
                ("בקטנה", "ק.ט.נ", "bektana", "v pohodě / maליčkost", "עזוב, זה בקטנה"),
                ("אחלה", "---", "achla", "skvělý / super", "אחלה יום"),
                ("כאילו", "כ.א.ל", "ke'ilu", "jako / jakoby", "זה כאילו חלום"),
                ("נראה לי", "ר.א.ה", "nir'e לי", "zdá se mi / myslím", "נראה לי שזה נכון"),
                ("יאללה", "---", "jalla", "tak pojď / שup", "יאללה, בוא נלך"),
                ("מביך", "ב.ו.ך", "mevich", "trapný / uvádějící do rozpaků", "סיטואציה מביכה")
            ],
            "grammar": [
                "Hebrejský slang je mix: <strong>סבבה</strong> pochází z arabשtiny, <strong>תכלס</strong> z jidiש (původně z heb. <em>tachליt</em> – účel).",
                "U slangových slov často neuvádíme kořeny, protože nejsou součástí původního hebrejského systému."
            ],
            "exercises": [
                ("היה לי מצב _______ מאוד אתמול.", "מביך"),
                ("_______, אין לי כוח לצאת היום.", "תכלס"),
                ("אל תדאג, זה _______, הכל בסדר.", "בקטנה")
            ],
            "topic": "slang"
        },
        {
            "id": "008",
            "title": "Zdraví a medicína",
            "heb_title": "בריאות ורפואה",
            "article": "כאשר מרגישים לא טוב, חשוב לקבוע תור לרופא בקופת החולים. הרופא מבצע בדיקה מקיפה כדי לאבחן את המחלה. אם יש כאב או דלקת, הרופא יכול לתת מרשם לתרופה מתאימה. לאחר קבלת הטיפול, מתחיל תהליך ההחלמה.",
            "vocab": [
                ("טיפול", "ט.פ.ל", "tipul", "léčba / péče", "טיפול רפואי"),
                ("בדיקה", "ב.ד.ק", "bdika", "kontrola / test", "בדיקת דם"),
                ("תרופה", "ר.פ.א", "trufa", "lék", "לקחת תרופה"),
                ("מרשם", "ר.ש.ם", "mirשam", "recept (lékařský)", "מרשם מהרופא"),
                ("מחלה", "ח.ל.ה", "machala", "nemoc", "מחלה קשה"),
                ("החלמה", "ח.ל.ם", "hachlama", "zotavení", "החלמה מהירה"),
                ("כאב", "כ.א.ב", "ke'ev", "bolest", "כאב ראש"),
                ("רגישות", "ר.ג.ש", "regišut", "citליvost / alergie", "רגישות לפניצילין"),
                ("דלקת", "ד.ל.ק", "daleket", "zánět", "דלקת גרון"),
                ("אבחנה", "ב.ח.ן", "abchana", "diagnóza", "אבחנה מדויקת")
            ],
            "grammar": [
                "Kořen <strong>ר.פ.א</strong> (R-P-A) souvisí s léčením. Najdeme ho ve slovech <em>rofe</em> (lékař), <em>trufa</em> (lék), <em>refua</em> (medicína).",
                "Předpona <strong>m-</strong> u slova <strong>מרשם</strong> (mirשam) naznačuje výsledek činnosti kořene <strong>ר.ש.ם</strong> (psát/zapisovat)."
            ],
            "exercises": [
                ("הרופא נתן לי _______ לתרופה.", "מרשם"),
                ("יש לי _______ חזק בגרון.", "דלקת"),
                ("אני מאחל לך _______ מהירה!", "החלמה")
            ],
            "topic": "zdraví"
        },
        {
            "id": "009",
            "title": "Příroda a cestování",
            "heb_title": "טבע וטיולים",
            "article": "הטבע בישראל מגוון מאוד, מהחרמון בצפון ועד אילת בדרום. ישראלים רבים אוהבים לצאת לטיולים בשמורות טבע וללכת במסלולים מאתגרים. הנוף מהרי הגולן עוצר נשימה. חשוב מאוד לשמור על הסביבה ולמנוע זיהום.",
            "vocab": [
                ("נוף", "נ.ו.ף", "nof", "výhled / krajina", "נוף מרהיב"),
                ("מסלול", "ס.ל.ל", "maslul", "trasa / cesta", "מסלול הליכה"),
                ("שמורה", "ש.מ.ר", "šmura", "rezervace", "שמורת טבע"),
                ("סביבה", "ס.ב.ב", "sviva", "prostředí", "איכות הסביבה"),
                ("זיהום", "ז.ה.ם", "zihum", "znečiשtění", "זיהום אוויר"),
                ("שימור", "ש.מ.ר", "šimur", "ochrana / konzervace", "שימור הטבע"),
                ("חופש", "ח.פ.ש", "chofeš", "svoboda / volno", "לצאת לחופש"),
                ("הרפתקה", "---", "harpatka", "dobrodružství", "הרפתקה גדולה"),
                ("אתר", "---", "atar", "místo / památka", "אתר מורשת"),
                ("מדריך", "ד.ר.ך", "madrich", "průvodce", "מדריך טיולים")
            ],
            "grammar": [
                "Předpona <strong>m-</strong> se často používá k vytvoření nástroje nebo osoby: <strong>מדריך</strong> (madrich) je ten, kdo ukazuje cestu (<em>derech</em>).",
                "Slovo <strong>שמורה</strong> (šmura) pochází z kořene <strong>ש.מ.ר</strong> (střežit/zachovávat)."
            ],
            "exercises": [
                ("הלכנו ב_______ הליכה יפה בהרים.", "מסלול"),
                ("ה_______ מהפסגה היה מדהים.", "נוף"),
                ("צריך לשמור על ה_______ שלנו.", "סביבה")
            ],
            "topic": "příroda"
        },
        {
            "id": "010",
            "title": "Věda a vzdělání",
            "heb_title": "חינוך ומדע",
            "article": "השכלה היא המפתח להצלחה בעידן המודרני. אוניברסיטאות בישראל נחשבות למוסדות מחקר מובילים בעולם. סטודנטים רבים לומדים לתואר ראשון ושני במגוון תחומים ומפתחים מיומנויות חדשות. הממשלה מעניקה מלגות לסטודנטים מצטיינים.",
            "vocab": [
                ("מחקר", "ח.ק.ר", "mechkar", "výzkum", "מחקר מדעי"),
                ("השכלה", "ש.כ.ל", "haskala", "vzdělání", "השכלה גבוהה"),
                ("מיומנות", "י.מ.נ", "mejummanut", "dovednost", "מיומנויות למידה"),
                ("שיעור", "ש.ע.ר", "ši'ur", "lekce / hodina", "ši'ur עברית"),
                ("מלגה", "מ.ל.ג", "milga", "stipendium", "קיבלתי מלגה"),
                ("מוסד", "י.ס.ד", "mosad", "instituce / ústav", "מוסד אקדמי"),
                ("תואר", "ת.א.ר", "to'ar", "titul (akademický)", "תואר ראשון"),
                ("ידע", "י.ד.ע", "jeda", "znalosti / vědění", "ידע רב"),
                ("למידה", "ל.מ.ד", "lemida", "učení se (proces)", "שיטות למידה"),
                ("גילוי", "ג.ל.ה", "giluj", "objev", "גילוי חדש")
            ],
            "grammar": [
                "Z kořene <strong>י.ד.ע</strong> (J-D-A) máme <em>jeda</em> (znalost), <em>muda'ut</em> (povědomí), <em>mada</em> (věda) a sloveso <em>lada'at</em> (vědět).",
                "Slovo <strong>השכלה</strong> (haskala) souvisí s inteליgencí a rozumem (<em>sechel</em>)."
            ],
            "exercises": [
                ("הוא קיבל _______ כדי ללמוד באוניברסיטה.", "מלגה"),
                ("ה_______ באוניברסיטה היה מעניין.", "שיעור"),
                ("היא לומדת ל_______ שני בביולוגיה.", "תואר")
            ],
            "topic": "věda"
        }
    ]

    html_template = """<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="main-header">
        <h1>Lekce {id_int}<br>{title}</h1>
        <div class="heb-title">({heb_title})</div>
    </div>
    
    <h3>1. Článek</h3>
    <div class="article-rtl">{article}</div>

    <h3>2. Slovíčka</h3>
    <table dir="ltr">
        <thead>
            <tr>
                <th>Hebrejsky</th>
                <th>Kořen</th>
                <th>Výslovnost</th>
                <th>Význam</th>
                <th>Příklad</th>
            </tr>
        </thead>
        <tbody>
            {vocab_rows}
        </tbody>
    </table>

    <h3>3. Gramatický výklad</h3>
    <div class="grammar-box">
        {grammar_points}
    </div>

    
    <h3>4. Cvičení</h3>
    <div class="grammar-box" style="background-color: #f9f9f9; border-right-color: #2ecc71;">
        <p><strong>Doplňte správné slovíčko z tabulky do vět:</strong></p>
        <ol>
            {exercise_ליnes}
        </ol>
        <p><small><em>(Nápověda: {hint})</em></small></p>
    </div>

    <h3>5. Slovíčka pro Anki</h3>
    <div class="anki-preview">
Hebrejsky;Kořen;Výslovnost;Význam;Příklad
{anki_rows}
    </div>

    <h3>6. Řešení cvičení</h3>
    <div class="grammar-box" style="background-color: #f0fff4; border-right-color: #27ae60;">
        <details>
            <summary>Klikněte pro zobrazení správných odpovědí</summary>
            <ol>
                {solutions}
            </ol>
        </details>
    </div>

</body>
</html>"""

    md_template = """# Lekce {id_int}: {title} ({heb_title})

## 1. Článek
{article}

## 2. Slovíčka
| Hebrejsky | Kořen | Výslovnost | Význam | Příklad |
| :--- | :--- | :--- | :--- | :--- |
{vocab_md_table}

## 3. Gramatický výklad
{grammar_md}

## 4. Cvičení
**Doplňte správné slovíčko z tabulky do vět:**
{exercise_md}

## 5. Řešení cvičení
{solutions_md}
"""

    for data in lessons_data:
        id_int = int(data["id"])
        
        # Vocab rows for HTML
        vocab_rows = ""
        for word, root, pron, mean, ex in data["vocab"]:
            vocab_rows += f'            <tr><td class="heb-word">{word}</td><td class="root-col">{root}</td><td class="pronun-col">{pron}</td><td class="meaning-col">{mean}</td><td class="example-rtl">{ex}</td></tr>\n'
        
        # Grammar points for HTML
        grammar_points = ""
        for point in data["grammar"]:
            grammar_points += f'        <p>{point}</p>\n'
            
        # Exercises and solutions
        exercise_ליnes = ""
        solutions = ""
        hint_words = [sol for ex, sol in data["exercises"]]
        import random
        shuffled_hints = list(hint_words)
        random.shuffle(shuffled_hints)
        hint = ", ".join(shuffled_hints)
        
        for ex, sol in data["exercises"]:
            exercise_ליnes += f'            <li>{ex}</li>\n'
            solutions += f'                <li>{sol}</li>\n'
            
        # Anki rows for HTML and CSV
        anki_rows = ""
        csv_content = "#Slovíčko;Kořen;Výslovnost;Význam;Příklad;Tag\n"
        for word, root, pron, mean, ex in data["vocab"]:
            anki_rows += f'{word};{root};{pron};{mean};{ex}\n'
            csv_content += f'{word};{root};{pron};{mean};{ex};{data["topic"]} lekce{data["id"]}\n'
            
        html_content = html_template.format(
            id_int=id_int,
            title=data["title"],
            heb_title=data["heb_title"],
            article=data["article"],
            vocab_rows=vocab_rows.strip(),
            grammar_points=grammar_points.strip(),
            exercise_ליnes=exercise_ליnes.strip(),
            hint=hint,
            anki_rows=anki_rows.strip(),
            solutions=solutions.strip()
        )
        
        # MD parts
        vocab_md_table = ""
        for word, root, pron, mean, ex in data["vocab"]:
            vocab_md_table += f'| {word} | {root} | {pron} | {mean} | {ex} |\n'
            
        grammar_md = "\n".join([p.replace("<strong>", "**").replace("</strong>", "**").replace("<em>", "*").replace("</em>", "*") for p in data["grammar"]])
        
        exercise_md = ""
        for i, (ex, sol) in enumerate(data["exercises"], 1):
            exercise_md += f'{i}. {ex}\n'
            
        solutions_md = ""
        for i, (ex, sol) in enumerate(data["exercises"], 1):
            solutions_md += f'{i}. {sol}\n'
            
        md_content = md_template.format(
            id_int=id_int,
            title=data["title"],
            heb_title=data["heb_title"],
            article=data["article"],
            vocab_md_table=vocab_md_table.strip(),
            grammar_md=grammar_md,
            exercise_md=exercise_md.strip(),
            solutions_md=solutions_md.strip()
        )
        
        # Write files
        with open(f"lekce{data['id']}.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        with open(f"lekce{data['id']}.md", "w", encoding="utf-8") as f:
            f.write(md_content)
        with open(f"anki_lekce{data['id']}.csv", "w", encoding="utf-8") as f:
            f.write(csv_content)
            
    print("Files generated successfully.")

if __name__ == "__main__":
    generate_lessons()
