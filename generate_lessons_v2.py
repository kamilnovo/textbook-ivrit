
import os

def generate_lessons():
    sidebar_links = [
        ('index.html', 'Úvod'),
        ('lekce001.html', 'Lekce 1: Média'),
        ('lekce002.html', 'Lekce 2: Technologie'),
        ('lekce003.html', 'Lekce 3: Práce'),
        ('lekce004.html', 'Lekce 4: Psychologie'),
        ('lekce005.html', 'Lekce 5: Právo'),
        ('lekce006.html', 'Lekce 6: Kultura'),
        ('lekce007.html', 'Lekce 7: Slang'),
        ('lekce008.html', 'Lekce 8: Zdraví'),
        ('lekce009.html', 'Lekce 9: Příroda'),
        ('lekce010.html', 'Lekce 10: Věda'),
        ('lekce011.html', 'Lekce 11: Společnost'),
        ('lekce012.html', 'Lekce 12: Život a práce'),
        ('lekce013.html', 'Lekce 13: Kultura a svátky')
    ]
    
    md_nav = ' | '.join([f'[Lekce {int(l[0][5:8])}]({l[0].replace(".html", ".md")})' for l in sidebar_links[1:]])

    lessons = [
        {
            'id': '001', 'title': 'Média a aktuality', 'heb': 'מדיה וחדשות',
            'article': 'הבוקר פורסם כי הממשלה החליטה להשקיע משאבים נוספים בשיפור התשתיות. השר הממונה ציין כי המהלך נועד לחזק את הכלכלה ולספק מקומות עבודה חדשים. התושבים מקווים כי המהלך יבוצע במהירות וישפר את איכות חייהם.',
            'vocab': [
                ('לפרסם', 'פ.ר.ס.ם', 'lefarsem', 'publikovat / zveřejnit', 'פורסם כי הממשלה החליטה'),
                ('ממשלה', 'מ.ש.ל', 'memšala', 'vláda', 'הממשלה החליטה להשקיע'),
                ('להשקיע', 'ש.ק.ע', 'lehaškia', 'investovat', 'להשקיע משאבים נוספים'),
                ('משאבים', 'ש.א.ב', 'mašavim', 'zdroje', 'משאבים כלכליים'),
                ('תשתית', 'ש.ת.ת', 'taštit', 'infrastruktura', 'שיפור התשתיות'),
                ('ממונה', 'מ.נ.ה', 'memune', 'pověřený / odpovědný', 'השר הממונה על הפרויקט'),
                ('מהלך', 'ה.ל.ך', 'mahalach', 'krok / proces / tah', 'המהלך נועד לחזק'),
                ('נועד', 'י.ע.ד', 'no\'ad', 'určen k / má za cíl', 'הפרויקט נועד לתושבים'),
                ('כלכלה', 'כ.ל.כ.ל', 'kalkala', 'ekonomika', 'הכלכלה המקומית חזקה'),
                ('תושב', 'י.ש.ב', 'tošav', 'obyvatel', 'התושבים גרים בצפון')
            ],
            'grammar': '<p>V textu vidíme pasivum <strong>פורסם</strong> (pursam) od slovesa <em>lefarsem</em>. V moderní hebrejštině se pasivum v médiích používá velmi často k vyjádření objektivity.</p><p>Kořen <strong>מ.ש.ל</strong> (M-Š-L) souvisí s vládnutím (memšala - vláda). Slovo <strong>תשתית</strong> (taštit - infrastruktura) vychází z kořene <strong>ש.ת.ת</strong>, který označuje zakládání nebo fundamenty.</p>',
            'exercise': [('הבוקר _______ כי הממשלה החליטה להשקיע.', 'פורסם'), ('המהלך _______ לחזק את הכלכלה.', 'נועד'), ('השר ה_______ על הפרויקט ביקר בצפון.', 'ממונה')],
            'tag': 'média'
        },
        {
            'id': '002', 'title': 'Technologie a high-tech', 'heb': 'טכנולוגיה והיי-טק',
            'article': 'ישראל ידועה בעולם כ"אומת הסטארט-אפ". חברות ישראליות רבות מפתחות טכנולוגיה חדשנית בתחומי הבינה המלאכותית והסייבר. כל חברה מנסה למצוא פתרון לבעיה גלובלית וליצור מוצר מוצלח שישרת מיליוני משתמשים ברחבי העולם. מרכז הפיתוח בתל אביב נחשב לאחד המובילים בעולם.',
            'vocab': [
                ('לפתח', 'פ.ת.ח', 'lefateach', 'vyvíjet / rozvíjet', 'לפתח טכנולוגיה חדשה'),
                ('חדשני', 'ח.ד.ש', 'chadašani', 'inovativní', 'מוצר חדשני ומעניין'),
                ('תחום', 'ת.ח.מ', 'tchum', 'obor / oblast', 'בתחום הבינה המלאכותית'),
                ('בינה מלאכותית', '---', 'bina melachutit', 'umělá inteligence', 'עתיד הבינה המלאכותית'),
                ('חברה', 'ח.ב.ר', 'chevra', 'společnost / firma', 'חברת סטארט-אפ'),
                ('פתרון', 'פ.ת.ר', 'pitron', 'řešení', 'למצוא פתרון לבעיה'),
                ('מוצר', 'י.צ.ר', 'mucar', 'produkt / výrobek', 'מוצר מוצלח מאוד'),
                ('משתמש', 'ש.מ.ש', 'mištameš', 'uživatel', 'מיליוני משתמשים בעולם'),
                ('פיתוח', 'פ.ת.ח', 'pituach', 'vývoj', 'מרכז פיתוח גדול'),
                ('מוצלח', 'צ.ל.ח', 'muclach', 'úspěšný', 'פרויקט מוצלח ורווחי')
            ],
            'grammar': '<p>Slovo <strong>פיתוח</strong> (pituach) je podstatné jméno slovesné od slovesa <strong>לפתח</strong> (lefateach). Tento vzor (ki-tu-ach) je typický pro kmen Pi\'el.</p><p>Slovo <strong>בינה</strong> (bina - inteligence) etymologicky souvisí s kořenem <strong>ב.י.נ</strong> (rozlišovat, chápat), ze kterého pochází i předložka <em>bejn</em> (mezi).</p>',
            'exercise': [('ישראל מפתחת _______ חדשנית.', 'טכנולוגיה'), ('החברה מצאה _______ לבעיה.', 'פתרון'), ('ה_______ בתל אביב נחשב למוביל.', 'מרכז הפיתוח')],
            'tag': 'technologie'
        },
        {
            'id': '003', 'title': 'Práce a kariéra', 'heb': 'עבודה וקריירה',
            'article': 'חיפוש עבודה בישראל דורש הכנה קפדנית. המועמד צריך לשלוח קורות חיים (קו"ח) מעודכnen ולהתכונן לראיון עבודה. במהלך הראיון, המעסיק בודק את הניסיון המקצועי của המועמד ואת היכולת שלו להשתלב בצוות. אם הראיון מוצלח, הצדדים חותמים על חוזה עבודה הכולל פרטים על המשכורת וההטבות.',
            'vocab': [
                ('ראיון', 'ר.א.ה', 'reajon', 'pohovor', 'ראיון עבודה'),
                ('קו"ח', 'ח.י.ה', 'korot chajim', 'životopis (CV)', 'שלחתי קו"ח'),
                ('מעסיק', 'ע.ס.ק', 'ma\'asik', 'zaměstnavatel', 'המעסיק שלי נחמד'),
                ('ניסיון', 'נ.ס.ה', 'nisajon', 'zkušenost', 'יש לי ניסיון רב'),
                ('משרה', 'ש.ר.ה', 'misra', 'pracovní pozice', 'משרה מלאה'),
                ('להתפטר', 'פ.ט.ר', 'lehitpater', 'dát výpověď', 'החלטתי להתפטר'),
                ('חוזה', 'ח.ז.ה', 'choze', 'smlouva', 'חתמנו על חוזה'),
                ('משכורת', 'ש.כ.ר', 'maschoret', 'plat / mzda', 'משכורת גבוהה'),
                ('הטבות', 'ט.ו.ב', 'hatavot', 'benefity', 'הטבות סוציאליות'),
                ('לקדם', 'ק.ד.ם', 'lekadem', 'povýšit / propagovat', 'הבוס רוצה לקדם אותי')
            ],
            'grammar': '<p>Kořen <strong>ש.כ.ר</strong> (S-K-R) souvisí s odměnou (sechar - mzda). Slovo <strong>ראיון</strong> (reajon) má kořen pro vidění (R-A-H), jde o "vzájemné prohlédnutí".</p><p>Slovo <strong>משרה</strong> (misra - pozice) etymologicky souvisí s autoritou a správou.</p>',
            'exercise': [('שלחתי _______ למעסיק.', 'קו"ח'), ('הצדדים חתמו על _______ עבודה.', 'חוזה'), ('אני מקווה לקבל _______ גבוהה.', 'משכורת')],
            'tag': 'práce'
        },
        {
            'id': '004', 'title': 'Psychologie a emoce', 'heb': 'פסיכולוגיה ורגשות',
            'article': 'הבריאות הנפשית חשובה לא פחות מהבריאות הפיזית. אנשים רבים סובלים מתחושת חרדה או דיכאון בגלל הלחץ המודרני. המודעות לחשיבות הטיפול הפסיכולוגי עלתה בשנים האחרונות. פיתוח ביטחון עצמי ומציאת מקורות של אושר פנימי יכולים לשפר את איכות החיים באופן משמעותי. זיכרון של חוויות חיוביות עוזר לנו להתמודד עם סבל וקשיים.',
            'vocab': [
                ('רגש', 'ר.ג.ש', 'regeš', 'emoce / cit', 'רגש חזק'),
                ('תחושה', 'ח.ו.ש', 'tchuša', 'pocit / vjem', 'תחושה של חופש'),
                ('דיכאון', 'ד.כ.א', 'dikaon', 'deprese', 'הוא סובל מדיכאון'),
                ('חרדה', 'ח.ר.ד', 'charada', 'úzkost / strach', 'התקף חרדה'),
                ('מודעות', 'י.ד.ע', 'muda\'ut', 'povědomí / uvědomění', 'מודעות עצמית'),
                ('ביטחון', 'ב.ט.ח', 'bitachon', 'bezpečí / sebevědomí', 'ביטחון עצמי'),
                ('אושר', 'א.ש.ר', 'ošer', 'štěstí', 'אושר אמיתי'),
                ('סבל', 'ס.ב.ל', 'sevel', 'utrpení', 'סבל פיזי'),
                ('זיכרון', 'ז.כ.ר', 'zikaron', 'paměť / vzpomínka', 'זיכרון לטווח ארוך'),
                ('השפעה', 'ש.פ.ע', 'hašpa\'a', 'vliv / dopad', 'השפעה חיובית')
            ],
            'grammar': '<p>Přípona <strong>-on</strong> se v hebrejštině často používá pro abstraktní pojmy a stavy (dikaon, zikaron, ra\'avon). Podstatné jméno <strong>תחושה</strong> (tchuša) má kořen <strong>ח.ו.ש</strong> (cítit).</p><p>Slovo <strong>אושר</strong> (ošer - štěstí) souvisí s kráčením přímo nebo potvrzením.</p>',
            'exercise': [('היא סובלת מ_______ בגלל המבחן.', 'חרדה'), ('יש לו _______ מצוין לשמות.', 'זיכרון'), ('הטיפול הפסיכולוגi העלה את ה_______.', 'מודעות')],
            'tag': 'psychologie'
        },
        {
            'id': '005', 'title': 'Právo a společnost', 'heb': 'משפט וחברה',
            'article': 'החוק במדינת ישראל מבטיח שוויון זכויות לכל האזרחים. כאשר אדם עובר על החוק, המשטרה חוקרת את המקרה והתובע מגיש כתב אישום לבית המשפט. במהלך המשפט, השופט מקשיב לעדויות של העדים ובוחן את הראיות. בסיום התהליך, השופט נותן פסק דין הקובע אם הנאשם אשם או זכאי.',
            'vocab': [
                ('חוק', 'ח.ק.ק', 'chok', 'zákon', 'לשמור על החוק'),
                ('זכות', 'ז.כ.ה', 'zchut', 'právo (nárok)', 'זכות הדיבור'),
                ('חובה', 'ח.ו.ב', 'chova', 'povinnost', 'חובות האזרח'),
                ('שופט', 'ש.פ.ט', 'šofet', 'soudce', 'השופט נתן פסק דין'),
                ('עורך דין', 'ע.ר.ך', 'orech din', 'advokát / právník', 'עורך דין פלילי'),
                ('אשם', 'א.ש.ם', 'ašam', 'vinný', 'הוא נמצא אשם'),
                ('עדות', 'ע.ו.ד', 'edut', 'svědectví', 'עדות בבית המשפט'),
                ('ראיה', 'ר.א.ה', 'reaja', 'důkaz', 'יש ראיות חזקות'),
                ('צדק', 'צ.ד.ק', 'cedek', 'spravedlnost', 'מערכת הצדק'),
                ('זכאי', 'ז.כ.ה', 'zakai', 'nevinný / oprávněný', 'הנאשם נמצא זכאי')
            ],
            'grammar': '<p>V právní hebrejštině je klíčová vazba <strong>smichut</strong> (beit mišpat - soud). Slovo <strong>חוק</strong> (chok) původně znamenalo něco vytesaného do kamene.</p><p>Slovo <strong>צדק</strong> (cedek - spravedlnost) je základem pro slovo <em>cadik</em> (spravedlivý člověk).</p>',
            'exercise': [('ה_______ בוחן את הראיות.', 'שופט'), ('לכל אדם יש _______ לייצוג.', 'זכות'), ('בית ה_______ נתן פסק דין.', 'משפט')],
            'tag': 'právo'
        },
        {
            'id': '006', 'title': 'Kultura a volný čas', 'heb': 'תרבות ופנאי',
            'article': 'התרבות הישראלית עשيرة ביצירתיות ובהשראה. בכל שנה מתקיימים פסטיבלים של מוזיקה, תיאטרון ואמנות ברחבי הארץ. תערוכה חדשה שנפתחה במוזיאון מציגה יצירות של אמנים צעירים. הקהל הישראלי אוהב הופעות חיות וממלא את האולמות. הביקורת בעיתון ציינה כי הסגנון של האמנים משלב בין מסורת למודרניות.',
            'vocab': [
                ('אמנות', 'א.מ.ן', 'amanut', 'umění', 'אמנות מודרנית'),
                ('יצירה', 'י.צ.ר', 'jecira', 'dílo / tvorba', 'יצירת מופת'),
                ('הופעה', 'י.פ.ע', 'hofa\'a', 'představení / koncert', 'הופעה חיה'),
                ('תערוכה', 'ע.ר.ך', 'ta\'arucha', 'výstava', 'תערוכה במוזיאון'),
                ('השראה', 'ש.ר.ה', 'hašra\'a', 'inspirace', 'קיבלתי השראה'),
                ('כישרון', 'כ.ש.ר', 'kišaron', 'talent', 'כישרון מוזיקלי'),
                ('קהל', 'ק.ה.ל', 'kahal', 'publika / dav', 'קהל גדול'),
                ('ביקורת', 'ב.ק.ר', 'bikoret', 'kritika / recenze', 'ביקורת חיובית'),
                ('סגנון', 'ס.ג.נ', 'signon', 'styl', 'סגנון אישי'),
                ('בילוי', 'ב.ל.ה', 'biluj', 'zábava / trávení času', 'בילוי עם חברים')
            ],
            'grammar': '<p>Slovo <strong>סגנון</strong> (signon) pochází z řeckého <em>signum</em> a do hebrejštiny se dostalo jako výraz pro styl. Podstatné jméno <strong>בילוי</strong> (biluj) je tvořeno z kmenu Pi\'el.</p><p>Kořen <strong>א.מ.ן</strong> (amanut - umění) je stejný jako ve slově <em>emun</em> (důvěra) nebo <em>amen</em>.</p>',
            'exercise': [('ה_______ מילא את האולם.', 'קהל'), ('האמנית קיבלה _______ מהטבע.', 'השראה'), ('זו _______ אמנות מרשימה.', 'יצירת')],
            'tag': 'kultura'
        },
        {
            'id': '007', 'title': 'Slang a idiomy', 'heb': 'סלנג וביטויים',
            'article': 'למרות שהעברית הרשמית יפה מאוד, ביומיום הישראלים משתמשים בסלנג רב. אם מישהו אומר לכם "חבל על הזמן", הוא בדרך כלל מתכוון שמשהו היה מצוין. המילה "תכלס" עוזרת לנו להגיע לעיקר השיחה. כשקורה משהו מביך, אנחנו קוראים לזה "פדיחה". בסופו של דבר, הכי חשוב שהכל יהיה "סבבה".',
            'vocab': [
                ('סבבה', '---', 'sababa', 'v pohodě / OK', 'הכל סבבה'),
                ('פדיחה', '---', 'fadicha', 'trapas / ostuda', 'הייתה לי פדיחה'),
                ('אשכרה', '---', 'aškara', 'fakt / vážně', 'הוא אשכרה אמר את זה'),
                ('תכלס', '---', 'tachles', 'vlastně / k věci', 'תכלס, אתה צודק'),
                ('בקטנה', 'ק.ט.נ', 'bektana', 'v pohodě / maličkost', 'עזוב, זה בקטנה'),
                ('אחלה', '---', 'achla', 'skvělý / super', 'אחלה יום שיהיה לך'),
                ('כאילו', 'כ.א.ל', 'ke\'ilu', 'jako / jakoby', 'זה כאילו חלום'),
                ('נראה לי', 'ר.א.ה', 'nir\'e li', 'zdá se mi / myslím', 'נראה לי שזה נכון'),
                ('יאללה', '---', 'jalla', 'tak pojď / šup', 'יאללה, בוא נלך'),
                ('מביך', 'ב.ו.ך', 'mevich', 'trapný', 'סיטואציה מביכה')
            ],
            'grammar': '<p>Hebrejský slang je mixem vlivů. <strong>סבבה</strong> je z arabštiny, <strong>תכלס</strong> z jidiš (původně z Tachlit - účel). </p><p>Slovo <strong>אשכרה</strong> (aškara) má původ v aramejštině a znamená "zjevně" nebo "skutečně".</p>',
            'exercise': [('הייתה לי _______ רצינית אתמול.', 'פדיחה'), ('_______, אתה ממש צודק.', 'תכלס'), ('הוא _______ לא ידע מזה.', 'אשכרה')],
            'tag': 'slang'
        },
        {
            'id': '008', 'title': 'Zdraví a medicína', 'heb': 'בריאות ורפואה',
            'article': 'כאשר מרגישים לא טוב, חשוב לקבוע תור לרופא בקופת החולים. הרופא מבצע בדיקה מקיפה כדי לאבחן את המחלה. אם יש כאב או דלקת, הרופא יכול לתת מרשם לתרופה מתאימה. במקרה של רגישות לתרופות, יש לעדכן את הצוות. לאחר הטיפול, מתחיל תהליך ההחלמה. חשוב להקשיב לגוף כדי לחזור לאיתנו.',
            'vocab': [
                ('טיפול', 'ט.פ.ל', 'tipul', 'léčba / péče', 'טיפול רפואی'),
                ('בדיקה', 'ב.ד.ק', 'bdika', 'kontrola / test', 'בדיקת דם'),
                ('תרופה', 'ר.פ.א', 'trufa', 'lék', 'לקחת תרופה'),
                ('מרשם', 'ר.ש.ם', 'miršam', 'recept', 'מרשם מהרופא'),
                ('מחלה', 'ח.ל.ה', 'machala', 'nemoc', 'מחלה קשה'),
                ('החלמה', 'ח.ל.ם', 'hachlama', 'zotavení', 'החלמה מהירה'),
                ('כאב', 'כ.א.ב', 'ke\'ev', 'bolest', 'כאב ראש'),
                ('רגישות', 'ר.ג.ש', 'regišut', 'citlivost / alergie', 'רגישות לפניצילין'),
                ('דלקת', 'ד.ל.ק', 'daleket', 'zánět', 'דלקת גרון'),
                ('אבחנה', 'ב.ח.ן', 'abchana', 'diagnóza', 'אבחנה מדויקת')
            ],
            'grammar': '<p>Kořen <strong>ר.פ.א</strong> (léčit) tvoří celou rodinu slov: <em>rofe</em> (lékař), <em>trufa</em> (lék), <em>refua</em> (medicína).</p><p>Slovo <strong>דלקת</strong> (daleket - zánět) souvisí s kořenem <strong>ד.ל.ק</strong> (hořet, zapálit), což přesně popisuje pocit při zánětu.</p>',
            'exercise': [('קיבלתי _______ לתרופה חדשה.', 'מרשם'), ('הוא סובל מ_______ גרון.', 'דלקת'), ('הרופא ביצע _______ מקיפה.', 'בדיקה')],
            'tag': 'zdraví'
        },
        {
            'id': '009', 'title': 'Příroda a cestování', 'heb': 'טבע וטיולים',
            'article': 'הטבע בישראל מגוון מאוד, מהחרמון בצפון ועד אילת בדרום. ישראלים רבים אוהבים לצאת לטיולים בשמורות טבע וללכת במסלולים מאתגרים. הנוף מהרי הגולן או מהרי אילת עוצר נשימה. חשוב מאוד לשמור על הסביבה ולמנוע זיהום כדי להגן על חיות הבר. מדריך טיולים מנוסה יכול להוסיף ידע רב על ההיסטוריה והגיאולוגיה.',
            'vocab': [
                ('נוף', 'נ.ו.ף', 'nof', 'výhled / krajina', 'נוף מרהיב'),
                ('מסלול', 'ס.ל.ל', 'maslul', 'trasa / cesta', 'מסלול הליכה'),
                ('שמורה', 'ש.מ.ר', 'šmura', 'rezervace', 'שמורת טבע'),
                ('סביבה', 'ס.ב.ב', 'sviva', 'prostředí', 'איכות הסביבה'),
                ('זיהום', 'ז.ה.ם', 'zihum', 'znečištění', 'זיהום אוויר'),
                ('שימור', 'ש.מ.ר', 'šimur', 'ochrana / konzervace', 'שימור הטבע'),
                ('חופש', 'ח.פ.ש', 'chofeš', 'svoboda / volno', 'לצאת לחופש'),
                ('הרפתקה', '---', 'harpatka', 'dobrodružství', 'הרפתקה גדולה'),
                ('אתר', '---', 'atar', 'místo / památka', 'אתר מורשת'),
                ('מדריך', 'ד.ר.ך', 'madrich', 'průvodce', 'מדריך טיולים')
            ],
            'grammar': '<p>Předpona <strong>מ</strong> se často používá k vytvoření místa (makom) nebo nástroje/osoby. <strong>מדריך</strong> (madrich) je ten, kdo ukazuje cestu (derech).</p><p>Slovo <strong>שמורה</strong> (šmura - rezervace) pochází z kořene <strong>ש.מ.ר</strong> (střežit, hlídat).</p>',
            'exercise': [('טיילנו ב_______ טבע יפה.', 'שמורת'), ('ה_______ מהר חרמון מדהים.', 'נוף'), ('צריך למנוע _______ בסביבה.', 'זיהום')],
            'tag': 'příroda'
        },
        {
            'id': '010', 'title': 'Vzdělání a věda', 'heb': 'חינוך ומדע',
            'article': 'השכלה היא המפתח להצלחה בעידן המודרני. אוניברסיטאות בישראל נחשבות למוסדות מחקר מובילים בעולם. סטודנטים רבים לומדים לתואר ראשון ושני ומפתחים מיומנויות חדשות. הממשלה מעניקה מלגות לסטודנטים מצטיינים כדי לעודד למידה וגילויים מדעיים. כל שיעור באוניברסיטה מרחיב את הידע והתפתחות.',
            'vocab': [
                ('מחקר', 'ח.ק.ר', 'mechkar', 'výzkum', 'מחקר מדעי'),
                ('השכלה', 'ש.כ.ל', 'haskala', 'vzdělání', 'השכלה גבוהה'),
                ('מיומנות', 'י.מ.נ', 'mejummanut', 'dovednost', 'מיומנויות למידה'),
                ('שיעור', 'ש.ע.ר', 'ši\'ur', 'lekce / hodina', 'שיעור עברית'),
                ('מלגה', 'מ.ל.ג', 'milga', 'stipendium', 'קיבלתי מלגה'),
                ('מוסד', 'י.ס.ד', 'mosad', 'instituce / ústav', 'מוסד אקדמי'),
                ('תואר', 'ת.א.ר', 'to\'ar', 'titul (akademický)', 'תואר ראשון'),
                ('ידע', 'י.ד.ע', 'jeda', 'znalosti / vědění', 'ידע רב'),
                ('למידה', 'ל.מ.ד', 'lemida', 'učení se (proces)', 'שיטות למידה'),
                ('גילוי', 'ג.ל.ה', 'giluj', 'objev', 'גילוי חדש')
            ],
            'grammar': '<p>Kořen <strong>י.ד.ע</strong> (vědět) tvoří slova: <em>jeda</em> (znalost), <em>muda\'ut</em> (povědomí), <em>mada</em> (věda).</p><p>Slovo <strong>השכלה</strong> (haskala - vzdělání) souvisí s intelektem (sechel). V 18. a 19. století se tak nazývalo židovské osvícenství.</p>',
            'exercise': [('הוא לומד לתואר _______ באוניברסיטה.', 'שני'), ('קיבלתי _______ למימון הלימודים.', 'מלגה'), ('האוניברסיטה היא _______ מחקר חשוב.', 'מוסד')],
            'tag': 'věda'
        },
        {
            'id': '011', 'title': 'Izraelská společnost', 'heb': 'חברה ודמוגרפיה',
            'article': 'החברה הישראלית מתאפיינת במגוון רחב של קבוצות ומגזרים. אחד הנושאים המרכזיים הוא המתח בין דתיים לחילונים. בשנים האחרונות גדלה המודעות לשילוב הציבור החרדי בשוק התעסוקה ובצה"ל. בנוסף, ישראל ממשיכה לקלוט עולים חדשים מרחבי העולם. כל מגזר שואף לשמור על הזהות הייחודית שלו, אך קיימת שאיפה לאחדות לאומית וסובלנות הדדית.',
            'vocab': [
                ('מגזר', 'ג.ז.ר', 'migzar', 'sektor / odvětví', 'המגזר החרדי'),
                ('חילוני', 'ח.ל.נ', 'chiloni', 'sekulární', 'בית ספר חילוני'),
                ('דתי', 'ד.ת', 'dati', 'náboženský', 'משפחה דתית'),
                ('חרדי', 'ח.ר.ד', 'charedi', 'ultraortodoxní', 'הציבור החרדי'),
                ('זהות', 'ז.ה.ה', 'zehut', 'identita', 'זהות לאומית'),
                ('עולה חדש', 'ע.ל.ה', 'ole chadaš', 'nový přistěhovalec', 'קליטת עולים חדשים'),
                ('סובלנות', 'ס.ב.ל', 'sovlanut', 'tolerance', 'סובלנות הדדית'),
                ('הדדי', 'ה.ד.ד', 'hadadi', 'vzájemný', 'כבוד הדדי'),
                ('קליטה', 'ק.ל.ט', 'klita', 'přijetí / absorpce', 'מרכז קליטה'),
                ('מתח', 'מ.ת.ח', 'metach', 'napětí / stres', 'מתח חברתי גבוה')
            ],
            'grammar': '<p>Kořen <strong>ס.ב.ל</strong> znamená „nést břemeno“. <strong>סובלנות</strong> (sovlanut - tolerance) je schopnost unést odlišnost druhého, zatímco <strong>סבלנות</strong> (savlanut - trpělivost) je schopnost nést břemeno času.</p><p>Slovo <strong>מגזר</strong> (migzar - sektor) souvisí s řezáním nebo vymezováním (gezer).</p>',
            'exercise': [('חשוב לגלות _______ כלפי האחר.', 'סובלנות'), ('הוא הגיע לישראל כ_______.', 'עולה חדש'), ('יש _______ גבוה בין הקבוצות.', 'מתח')],
            'tag': 'společnost'
        },
        {
            'id': '012', 'title': 'Život a práce v Izraeli', 'heb': 'חיים ועבודה בישראל',
            'article': 'החיים בישראל משלבים בין עבודה אינטנסיבית לבין דגש חזק על משפחה ופנאי. מושג ה"וורק-לייף באלאנס" הופך ליותר פופולרי, אך עדיין ישראלים רבים עובדים שעות נוספות. שירות המילואים משפיע על שוק העבודה ועל החיים האישיים. בתקופות של חופش, הישראלים אוהבים לטייל או לטוס לחו"ל. למרות הלחץ, קיימת תחושה של ערבות הדדית וסיוע בעת צרה.',
            'vocab': [
                ('פנאי', 'פ.נ.י', 'pnaj', 'volný čas', 'תרבות הפנאי'),
                ('שעות נוספות', 'י.ס.ף', 'ša\'ot nosafot', 'přesčasy', 'לעבוד שעות נוספות'),
                ('מילואים', 'מ.ל.א', 'miluim', 'vojenská záloha', 'שירות מילואים פעיל'),
                ('חופש', 'ח.פ.ש', 'chofeš', 'dovolená / svoboda', 'לצאת לחופש שנתי'),
                ('חו"ל', '---', 'chul', 'zahraničí', 'לטוס לחו"ל בקיץ'),
                ('ערבות', 'ע.ר.ב', 'aravut', 'záruka / ručení', 'ערבות הדדית'),
                ('צרה', 'צ.ר.ר', 'cara', 'potíž / neštěstí', 'חבר בעת צרה'),
                ('אתגר', 'ת.ג.ר', 'etgar', 'výzva', 'אתגר מקצועי חדש'),
                ('שגרה', 'ש.ג.ר', 'šigra', 'rutina', 'לחזור לשגרה'),
                ('איזון', 'א.ז.נ', 'izun', 'rovnováha / balans', 'איזון בין עבודה לבית')
            ],
            'grammar': '<p>Kořen <strong>מ.ל.א</strong> znamená „plný“ nebo „naplnit“. <strong>מילואים</strong> (miluim - záloha) původně znamenalo „doplnění“ nebo „výplň“ armády.</p><p>Slovo <strong>שגרה</strong> (šigra - rutina) souvisí s posíláním nebo plynulým tokem (š-g-r).</p>',
            'exercise': [('הוא נקרא לשירות _______.', 'מילואים'), ('צריך למצוא _______ בין עבודה למשפחה.', 'איזון'), ('הם טסים ל_______ בקיץ.', 'חו"ל')],
            'tag': 'práce'
        },
        {
            'id': '013', 'title': 'Kultura a svátky', 'heb': 'תרבות וחגים לאומיים',
            'article': 'התרבות הישראלית היא פסיפס מרתק של מסורת יהודית ומודרניות מערבית. החגים הלאומיים, כמו יום העצמאות ויום הזיכרון, ממלאים תפקי드 מרכזי. ביום העצמאות נהוג לערוך פיקניקים ולצפות במטס של חיל האוויר, בעוד שביום הזיכרון שוררת אווירה של הזכרה עם הנופלים. מוזיקה ישראלית משקפת את הגעגועים והתקוות של החברה.',
            'vocab': [
                ('תרבות', 'ר.ב.ה', 'tarbut', 'kultura', 'תרבות ישראלית'),
                ('פסיפס', '---', 'psifas', 'mozaika', 'פסיפס מרתק'),
                ('מסורת', 'מ.ס.ר', 'masoret', 'tradice', 'מסורת יהודית'),
                ('לאומי', 'ל.א.ם', 'le\'umi', 'národní', 'חגים לאומיים'),
                ('עצמאות', 'ע.צ.ם', 'acma\'ut', 'nezávislost', 'יום העצמאות'),
                ('זיכרון', 'ז.כ.ר', 'zikaron', 'paměť / vzpomínka', 'יום הזיכרון'),
                ('מטס', 'ט.ו.ס', 'matas', 'letecká přehlídka', 'מטס חיל האוויר'),
                ('הזכרה', 'ז.כ.ר', 'hazkara', 'vzpomínkový obřad / pieta', 'טקס הזכרה'),
                ('געגוע', 'ג.ע.ג.ע', 'ga\'agua', 'stesk / touha', 'געגועים ותקוות'),
                ('תקווה', 'ק.ו.ה', 'tikva', 'naděje', 'התקווה היא ההמנון')
            ],
            'grammar': '<p>Vazba <strong>smichut</strong> je klíčová pro názvy svátků (Jom ha-Acma\'ut). Kořen <strong>ר.ב.ה</strong> (množit se) tvoří slovo <strong>תרבות</strong> (tarbut - to, co se pěstuje/rozvíjí).</p><p>Slovo <strong>פסיפס</strong> (psifas - mozaika) je přejímka z řeckého <em>psēphos</em> (kamínek).</p>',
            'exercise': [('ביום העצמאות יש _______ של חיל האוויר.', 'מטס'), ('החברה הישראלית היא _______ של תרבויות.', 'פסיפס'), ('אנחנו הולכים לטקס _______.', 'הזכרה')],
            'tag': 'kultura'
        }
    ]

    for lesson in lessons:
        l_id = lesson['id']
        l_num = int(l_id)
        
        # HTML
        html_sidebar = '<div class=\"sidebar\"><h2>Obsah</h2>'
        for link, name in sidebar_links:
            active = ' class=\"active\"' if link == f'lekce{l_id}.html' else ''
            html_sidebar += f'<a href=\"{link}\"{active}>{name}</a>'
        html_sidebar += '</div>'
        
        html = f"""<!DOCTYPE html>
<html lang=\"cs\">
<head>
    <meta charset=\"UTF-8\">
    <link rel=\"stylesheet\" href=\"style.css\">
    <title>Lekce {l_num}</title>
</head>
<body>
    {html_sidebar}
    <div class=\"content\">
        <div class=\"main-header\">
            <h1>Lekce {l_num}<br>{lesson['title']}</h1>
            <div class=\"heb-title\">({lesson['heb']})</div>
        </div>
        <h3>1. Článek</h3>
        <div class=\"article-rtl\">{lesson['article']}</div>
        <h3>2. Slovíčka</h3>
        <table dir=\"ltr\">
            <thead><tr><th>Hebrejsky</th><th>Kořen</th><th>Výslovnost</th><th>Význam</th><th>Příklad</th></tr></thead>
            <tbody>"""
        for v in lesson['vocab']:
            html += f"<tr><td class='heb-word'>{v[0]}</td><td class='root-col'>{v[1]}</td><td class='pronun-col'>{v[2]}</td><td class='meaning-col'>{v[3]}</td><td class='example-rtl'>{v[4]}</td></tr>"
        
        html += f"""</tbody></table>
        <h3>3. Gramatický výklad</h3>
        <div class=\"grammar-box\">{lesson['grammar']}</div>
        <h3>4. Cvičení</h3>
        <div class=\"grammar-box\" style=\"background-color: #f9f9f9; border-right-color: #2ecc71;\"><ol>"""
        for ex in lesson['exercise']:
            html += f"<li>{ex[0]}</li>"
        html += f"""</ol></div>
        <h3>5. Slovíčka pro Anki</h3>
        <div class=\"anki-preview\">#Slovíčko;Kořen;Výslovnost;Význam;Příklad;Tag\n"""
        for v in lesson['vocab']:
            html += f"{v[0]};{v[1]};{v[2]};{v[3]};{v[4]};{lesson['tag']} lekce{l_id}\n"
        html += f"""</div>
        <h3>6. Řešení cvičení</h3>
        <div class=\"grammar-box\" style=\"background-color: #f0fff4; border-right-color: #27ae60;\">
            <details><summary>Klikněte pro zobrazení</summary><ol>"""
        for ex in lesson['exercise']:
            html += f"<li>{ex[1]}</li>"
        html += """</ol></details></div></div></body></html>"""
        
        with open(f'lekce{l_id}.html', 'w', encoding='utf-8') as f:
            f.write(html)

        # CSV
        csv_data = "#Slovíčko;Kořen;Výslovnost;Význam;Příklad;Tag\n"
        for v in lesson['vocab']:
            csv_data += f"{v[0]};{v[1]};{v[2]};{v[3]};{v[4]};{lesson['tag']} lekce{l_id}\n"
        with open(f'anki_lekce{l_id}.csv', 'w', encoding='utf-8-sig') as f:
            f.write(csv_data)

        # MD
        md = f"# Lekce {l_num}: {lesson['title']}\n\n{md_nav}\n\n## 1. Článek\n{lesson['article']}\n\n## 2. Slovíčka\n| Hebrejsky | Kořen | Výslovnost | Význam | Příklad |\n|---|---|---|---|---|\n"
        for v in lesson['vocab']:
            md += f"| {v[0]} | {v[1]} | {v[2]} | {v[3]} | {v[4]} |\n"
        md += f"\n## 3. Gramatika\n{lesson['grammar']}\n\n## 4. Cvičení\n"
        for ex in lesson['exercise']:
            md += f"1. {ex[0]}\n"
        md += f"\n## 5. Anki náhled\n```text\n#Slovíčko;Kořen;Výslovnost;Význam;Příklad;Tag\n"
        for v in lesson['vocab']:
            md += f"{v[0]};{v[1]};{v[2]};{v[3]};{v[4]};{lesson['tag']} lekce{l_id}\n"
        md += f"```\n\n## 6. Řešení\n"
        for ex in lesson['exercise']:
            md += f"* {ex[1]}\n"
        
        with open(f'lekce{l_id}.md', 'w', encoding='utf-8') as f:
            f.write(md)

if __name__ == '__main__':
    generate_lessons()
    print("Všech 13 lekcí bylo úspěšně vygenerováno.")
