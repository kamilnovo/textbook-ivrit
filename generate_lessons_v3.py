import os

def generate_lessons():
    import time
    version = int(time.time())
    # Define sidebar links for all 20 lessons + index.html
    sidebar_links = [('index.html', 'Úvod')]
    lesson_titles = [
        "Média a aktuality", "Technologie a high-tech", "Práce a kariéra", 
        "Psychologie a emoce", "Právo a společnost", "Kultura a volný čas",
        "Slang a idiomy", "Zdraví a medicína", "Příroda a cestování",
        "Vzdělání a věda", "Izraelská společnost", "Život a práce v Izraeli",
        "Kultura a svátky", "Válka a bezpečnost", "Gastronomie a jídlo",
        "Historie a Jeruzalém", "Moderní Tel Aviv", "Příroda a Počasí",
        "Doprava a infrastruktura", "Izraelská rodina a sny"
    ]
    
    for i, title in enumerate(lesson_titles, 1):
        sidebar_links.append((f'lekce{i:03d}.html', f'Lekce {i}: {title}'))

    md_nav = ' | '.join([f'[Lekce {int(l[0][5:8])}]({l[0].replace(".html", ".md")})' for l in sidebar_links[1:]])

    lessons = [
        {
            'id': '001', 'title': 'Média a aktuality', 'heb': 'מדיה וחדשות', 'tag_topic': 'média',
            'article': 'הבוקר פורסם כי הממשלה החליטה להשקיע משאבים נוספים בשיפור התשתיות. השר הממונה ציין כי המהלך נועד לחזק את הכלכלה ולספק מקומות עבודה חדשים. התושבים מקווים כי המהלך יבוצע במהירות וישפר את איכות חייהם.',
            'vocab': [
                ('לפרסם', 'פ.ר.ס.ם', 'lefarsem', 'publikovat / zveřejnit', 'פורסם כי הממשלה החליטה', 'sloveso'),
                ('ממשלה', 'מ.ש.ל', 'memšala', 'vláda', 'הממשלה החליטה להשקיע', 'podst_jméno'),
                ('להשקיע', 'ש.ק.ע', 'lehaškia', 'investovat', 'להשקיע משאבים נוספים', 'sloveso'),
                ('משאבים', 'ש.א.ב', 'mašavim', 'zdroje', 'משאבים כלכליים', 'podst_jméno'),
                ('תשתית', 'ש.ת.ת', 'taštit', 'infrastruktura', 'שיפור התשתיות', 'podst_jméno'),
                ('ממונה', 'מ.נ.ה', 'memune', 'pověřený / odpovědný', 'השר הממונה על הפרויקט', 'příd_jméno'),
                ('מהלך', 'ה.ל.ך', 'mahalach', 'krok / proces / tah', 'המהלך נועד לחזק', 'podst_jméno'),
                ('נועד', 'י.ע.ד', 'no\'ad', 'určen k / má za cíl', 'הפרויקט נועד לתושבים', 'sloveso'),
                ('כלכלה', 'כ.ל.כ.ל', 'kalkala', 'ekonomika', 'הכלכלה המקומית חזקה', 'podst_jméno'),
                ('תושב', 'י.ש.ב', 'tošav', 'obyvatel', 'התושבים גרים בצפון', 'podst_jméno')
            ],
            'grammar': '<p>V textu vidíme pasivum <strong>פורסם</strong> (pursam) od slovesa <em>lefarsem</em>. V moderní hebrejštině se pasivum v médiích používá velmi často k vyjádření objektivity.</p><p>Kořen <strong>מ.ש.ל</strong> (M-Š-L) souvisí s vládnutím (memšala - vláda). Slovo <strong>תשתית</strong> (taštit - infrastruktura) vychází z kořene <strong>ש.ת.ת</strong>, který označuje zakládání nebo fundamenty.</p>',
            'exercise': [('הבוקר _______ כי הממשלה החליטה להשקיע.', 'פורסם'), ('המהלך _______ לחזק את הכלכלה.', 'נועד'), ('השר ה_______ על הפרויקט ביקר בצפון.', 'ממונה')]
        },
        {
            'id': '002', 'title': 'Technologie a high-tech', 'heb': 'טכנולוגיה והיי-טק', 'tag_topic': 'technologie',
            'article': 'ישראל ידועה בעולם כ"אומת הסטארט-אפ". חברות ישראליות רבות מפתחות טכנולוגיה חדשנית בתחומי הבינה המלאכותית והסייבר. כל חברה מנסה למצוא פתרון לבעיה גלובלית וליצור מוצר מוצלח שישרת מיליוני משתמשים ברחבי העולם. מרכז הפיתוח בתל אביב נחשב לאחד המובילים בעולם.',
            'vocab': [
                ('לפתח', 'פ.ת.ח', 'lefateach', 'vyvíjet / rozvíjet', 'לפתח טכנולוגיה חדשה', 'sloveso'),
                ('חדשני', 'ח.ד.ש', 'chadašani', 'inovativní', 'מוצר חדשני ומעניין', 'příd_jméno'),
                ('תחום', 'ת.ח.מ', 'tchum', 'obor / oblast', 'בתחום הבינה המלאכותית', 'podst_jméno'),
                ('בינה מלאכותית', '---', 'bina melachutit', 'umělá inteligence', 'עתיד הבינה המלאכותית', 'fráze'),
                ('חברה', 'ח.ב.ר', 'chevra', 'společnost / firma', 'חברת סטארט-אפ', 'podst_jméno'),
                ('פתרון', 'פ.ת.ר', 'pitron', 'řešení', 'למצוא פתרון לבעיה', 'podst_jméno'),
                ('מוצר', 'י.צ.ר', 'mucar', 'produkt / výrobek', 'מוצר מוצלח מאוד', 'podst_jméno'),
                ('משתמש', 'ש.מ.ש', 'mištameš', 'uživatel', 'מיליוני משתמשים בעולם', 'podst_jméno'),
                ('פיתוח', 'פ.ת.ח', 'pituach', 'vývoj', 'מרכז פיתוח גדול', 'podst_jméno'),
                ('מוצלח', 'צ.ל.ח', 'muclach', 'úspěšný', 'פרויקט מוצלח ורווחי', 'příd_jméno')
            ],
            'grammar': '<p>Slovo <strong>פיתוח</strong> (pituach) je podstatné jméno slovesné od slovesa <strong>לפתח</strong> (lefateach). Tento vzor (ki-tu-ach) je typický pro kmen Pi\'el.</p><p>Slovo <strong>בינה</strong> (bina - inteligence) etymologicky souvisí s kořenem <strong>ב.י.נ</strong> (rozlišovat, chápat), ze kterého pochází i předložka <em>bejn</em> (mezi).</p>',
            'exercise': [('ישראל מפתחת _______ חדשנית.', 'טכנולוגיה'), ('החברה מצאה _______ לבעיה.', 'פתרון'), ('ה_______ בתל אביב נחשב למוביל.', 'מרכז הפיתוח')]
        },
        {
            'id': '003', 'title': 'Práce a kariéra', 'heb': 'עבודה וקריירה', 'tag_topic': 'práce',
            'article': 'חיפוש עבודה בישראל דורש הכנה קפדנית. המועמד צריך לשלוח קורות חיים (קו"ח) מעודכנים ולהתכונן לראיון עבודה. במהלך הראיון, המעסיק בודק את הניסיון המקצועי של המועמד ואת היכולת שלו להשתלב בצוות. אם הראיון מוצלח, הצדדים חותמים על חוזה עבודה הכולל פרטים על המשכורת וההטבות.',
            'vocab': [
                ('ראיון', 'ר.א.ה', 'reajon', 'pohovor', 'ראיון עבודה', 'podst_jméno'),
                ('קו"ח', 'ח.י.ה', 'korot chajim', 'životopis (CV)', 'שלחתי קו"ח', 'fráze'),
                ('מעסיק', 'ע.ס.ק', 'ma\'asik', 'zaměstnavatel', 'המעסיק שלי נחמד', 'podst_jméno'),
                ('ניסיון', 'נ.ס.ה', 'nisajon', 'zkušenost', 'יש לי ניסיון רב', 'podst_jméno'),
                ('משרה', 'ש.ר.ה', 'misra', 'pracovní pozice', 'משרה מלאה', 'podst_jméno'),
                ('להתפטר', 'פ.ט.ר', 'lehitpater', 'dát výpověď', 'החלטתי להתפטר', 'sloveso'),
                ('חוזה', 'ח.ז.ה', 'choze', 'smlouva', 'חתמנו על חוזה', 'podst_jméno'),
                ('משכורת', 'ש.כ.ר', 'maschoret', 'plat / mzda', 'משכורת גבוהה', 'podst_jméno'),
                ('הטבות', 'ט.ו.ב', 'hatavot', 'benefity', 'הטבות סוציאליות', 'podst_jméno'),
                ('לקדם', 'ק.ד.ם', 'lekadem', 'povýšit / propagovat', 'הבוס רוצה לקדם אותי', 'sloveso')
            ],
            'grammar': '<p>Kořen <strong>ש.כ.ר</strong> (S-K-R) souvisí s odměnou (sechar - mzda). Slovo <strong>ראיון</strong> (reajon) má kořen pro vidění (R-A-H), jde o "vzájemné prohlédnutí".</p><p>Slovo <strong>משרה</strong> (misra - pozice) etymologicky souvisí s autoritou a správou.</p>',
            'exercise': [('שלחתי _______ למעסיק.', 'קו"ח'), ('הצדדים חתמו על _______ עבודה.', 'חוזה'), ('אני מקווה לקבל _______ גבוהה.', 'משכורת')]
        },
        {
            'id': '004', 'title': 'Psychologie a emoce', 'heb': 'פסיכולוגיה ורגשות', 'tag_topic': 'psychologie',
            'article': 'הבריאות הנפשית חשובה לא פחות מהבריאות הפיזית. אנשים רבים סובלים מתחושת חרדה או דיכאון בגלל הלחץ המודרני. המודעות לחשיבות הטיפול הפסיכולוגי עלתה בשנים האחרונות. פיתוח ביטחון עצמי ומציאת מקורות של אושר פנימי יכולים לשפר את איכות החיים באופן משמעותי. זיכרון של חוויות חיוביות עוזר לנו להתמודד s סבל וקשיים.',
            'vocab': [
                ('רגש', 'ר.ג.ש', 'regeš', 'emoce / cit', 'רגש חזק', 'podst_jméno'),
                ('תחושה', 'ח.ו.ש', 'tchuša', 'pocit / vjem', 'תחושה של חופש', 'podst_jméno'),
                ('דיכאון', 'ד.כ.א', 'dikaon', 'deprese', 'הוא סובל מדיכאון', 'podst_jméno'),
                ('חרדה', 'ח.ר.ד', 'charada', 'úzkost / strach', 'התקף חרדה', 'podst_jméno'),
                ('מודעות', 'י.ד.ע', 'muda\'ut', 'povědomí / uvědomění', 'מודעות עצמית', 'podst_jméno'),
                ('ביטחון', 'ב.ט.ח', 'bitachon', 'bezpečí / sebevédomí', 'ביטחון עצמי', 'podst_jméno'),
                ('אושר', 'א.ש.ר', 'ošer', 'štěstí', 'אושר אמיתי', 'podst_jméno'),
                ('סבל', 'ס.ב.ל', 'sevel', 'utrpení', 'סבל פיזי', 'podst_jméno'),
                ('זיכרון', 'ז.כ.ר', 'zikaron', 'paměť / vzpomínka', 'זיכרון לטווח ארוך', 'podst_jméno'),
                ('השפעה', 'ש.פ.ע', 'hašpa\'a', 'vliv / dopad', 'השפעה חיובית', 'podst_jméno')
            ],
            'grammar': '<p>Přípona <strong>-on</strong> se v hebrejštině často používá pro abstraktní pojmy a stavy (dikaon, zikaron, ra\'avon). Podstatné jméno <strong>תחושה</strong> (tchuša) má kořen <strong>ח.ו.ש</strong> (cítit).</p><p>Slovo <strong>אושר</strong> (ošer - štěstí) souvisí s kráčením přímo nebo potvrzením.</p>',
            'exercise': [('היא סובלת מ_______ בגלל המבחן.', 'חרדה'), ('יש לו _______ מצוין לשמות.', 'זיכרון'), ('הטיפול הפסיכולוגי העלה את ה_______.', 'מודעות')]
        },
        {
            'id': '005', 'title': 'Právo a společnost', 'heb': 'משפט וחברה', 'tag_topic': 'právo',
            'article': 'החוק במדינת ישראל מבטיח שוויון זכויות לכל האזרחים. כאשר אדם עובר על החוק, המשטרה חוקרת את המקרה והתובע מגיש כתב אישום לבית המשפט. במהלך המשפט, השופט מקשיב לעדויות של העדים ובוחן את הראיות. בסיום התהליך, השופט נותן פסק דין הקובע אם הנאשם אשם או זכאי.',
            'vocab': [
                ('חוק', 'ח.ק.ק', 'chok', 'zákon', 'לשמור על החוק', 'podst_jméno'),
                ('זכות', 'ז.כ.ה', 'zchut', 'právo (nárok)', 'זכות הדיבור', 'podst_jméno'),
                ('חובה', 'ח.ו.ב', 'chova', 'povinnost', 'חובות האזרח', 'podst_jméno'),
                ('שופט', 'ש.פ.ט', 'šofet', 'soudce', 'השופט נתן פסק דין', 'podst_jméno'),
                ('עורך דין', 'ע.ר.ך', 'orech din', 'advokát / právník', 'עורך דין פלילי', 'podst_jméno'),
                ('אשם', 'א.ש.ם', 'ašam', 'vinný', 'הוא נמצא אשם', 'příd_jméno'),
                ('עדות', 'ע.ו.ד', 'edut', 'svědectví', 'עדות בבית המשפט', 'podst_jméno'),
                ('ראיה', 'ר.א.ה', 'reaja', 'důkaz', 'יש ראיות חזקות', 'podst_jméno'),
                ('צדק', 'צ.ד.ק', 'cedek', 'spravedlnost', 'מערכת הצדק', 'podst_jméno'),
                ('זכאי', 'ז.כ.ה', 'zakai', 'nevinný / oprávněný', 'הנאשם נמצא זכאי', 'příd_jméno')
            ],
            'grammar': '<p>V právní hebrejštině je klíčová vazba <strong>smichut</strong> (beit mišpat - soud). Slovo <strong>חוק</strong> (chok) původně znamenalo něco vytesaného do kamene.</p><p>Slovo <strong>צדק</strong> (cedek - spravedlnost) je základem pro slovo <em>cadik</em> (spravedlivý člověk).</p>',
            'exercise': [('ה_______ בוחן את הראיות.', 'שופט'), ('לכל אדם יש _______ לייצוג.', 'זכות'), ('בית ה_______ נתן פסק דין.', 'משפט')]
        },
        {
            'id': '006', 'title': 'Kultura a volný čas', 'heb': 'תרבות ופנאי', 'tag_topic': 'kultura',
            'article': 'התרבות הישראלית עשירה ביצירתיות ובהשראה. בכל שנה מתקיימים פסטיבלים של מוזיקה, תיאטרון ואמנות ברחבי הארץ. תערוכה חדשה שנפתחה במוזיאון מציגה יצירות של אמנים צעירים. הקהל הישראלי אוהב הופעות חיות וממלא את האולמות. הביקורת בעיתון ציינה כי הסגנון של האמנים משלב בין מסורת למודרניות.',
            'vocab': [
                ('אמנות', 'א.מ.ן', 'amanut', 'umění', 'אמנות מודרנית', 'podst_jméno'),
                ('יצירה', 'י.צ.ר', 'jecira', 'dílo / tvorba', 'יצירת מופת', 'podst_jméno'),
                ('הופעה', 'י.פ.ע', 'hofa\'a', 'představení / koncert', 'הופעה חיה', 'podst_jméno'),
                ('תערוכה', 'ע.ר.ך', 'ta\'arucha', 'výstava', 'תערוכה במוזיאון', 'podst_jméno'),
                ('השראה', 'ש.ר.ה', 'hašra\'a', 'inspirace', 'קיבלתי השראה', 'podst_jméno'),
                ('כישרון', 'כ.ש.ר', 'kišaron', 'talent', 'כישרון מוזיקלי', 'podst_jméno'),
                ('קהל', 'ק.ה.ל', 'kahal', 'publika / dav', 'קהל גדול', 'podst_jméno'),
                ('ביקורת', 'ב.ק.ר', 'bikoret', 'kritika / recenze', 'ביקורת חיובית', 'podst_jméno'),
                ('סגנון', 'ס.ג.נ', 'signon', 'styl', 'סגנון אישי', 'podst_jméno'),
                ('בילוי', 'ב.ל.ה', 'biluj', 'zábava / trávení času', 'בילוי עם חברים', 'podst_jméno')
            ],
            'grammar': '<p>Slovo <strong>סגנון</strong> (signon) pochází z řeckého <em>signum</em> a do hebrejštiny se dostalo jako výraz pro styl. Podstatné jméno <strong>בילוי</strong> (biluj) je tvořeno z kmenu Pi\'el.</p><p>Kořen <strong>א.מ.ן</strong> (amanut - umění) je stejný jako ve slově <em>emun</em> (důvěra) nebo <em>amen</em>.</p>',
            'exercise': [('ה_______ מילא את האולם.', 'קהל'), ('האמנית קיבלה _______ מהטבע.', 'השראה'), ('זו _______ אמנות מרשימה.', 'יצירת')]
        },
        {
            'id': '007', 'title': 'Slang a idiomy', 'heb': 'סלנג וביטויים', 'tag_topic': 'slang',
            'article': 'למרות שהעברית הרשמית יפה מאוד, ביומיום הישראלים משתמשים בסלנג רב. אם מישהו אומר לכם "חבל על הזמן", הוא בדרך כלל מתכוון שמשהו היה מצוין. המילה "תכלס" עוזרת לנו להגיע לעיקר השיחה. כשקורה משהו מביך, אנחנו קוראים לזה "פדיחה". בסופו של דבר, הכי חשוב שהכל יהיה "סבבה".',
            'vocab': [
                ('סבבה', '---', 'sababa', 'v pohodě / OK', 'הכל סבבה', 'příslovce'),
                ('פדיחה', '---', 'fadicha', 'trapas / ostuda', 'הייתה לי פדיחה', 'podst_jméno'),
                ('אשכרה', '---', 'aškara', 'fakt / vážně', 'הוא אשכרה אמר את זה', 'příslovce'),
                ('תכלס', '---', 'tachles', 'vlastně / k věci', 'תכלס, אתה צודק', 'příslovce'),
                ('בקטנה', 'ק.ט.נ', 'bektana', 'v pohodě / maličkost', 'עזוב, זה בקטנה', 'fráze'),
                ('אחלה', '---', 'achla', 'skvělý / super', 'אחלה יום שיהיה לך', 'příd_jméno'),
                ('כאילו', 'כ.א.ל', 'ke\'ilu', 'jako / jakoby', 'זה כאילו חלום', 'příslovce'),
                ('נראה לי', 'ר.א.ה', 'nir\'e li', 'zdá se mi / myslím', 'נראה לי שזה נכון', 'fráze'),
                ('יאללה', '---', 'jalla', 'tak pojď / šup', 'יאללה, בוא נלך', 'fráze'),
                ('מביך', 'ב.ו.ך', 'mevich', 'trapný', 'סיטואציה מביכה', 'příd_jméno')
            ],
            'grammar': '<p>Hebrejský slang je mixem vlivů. <strong>סבבה</strong> je z arabštiny, <strong>תכלס</strong> z jidiš (původně z Tachlit - účel). </p><p>Slovo <strong>אשכרה</strong> (aškara) má původ v aramejštině a znamená "zjevně" nebo "skutečně".</p>',
            'exercise': [('הייתה לי _______ רצינית אתמול.', 'פדיחה'), ('_______, אתה ממש צודק.', 'תכלס'), ('הוא _______ לא ידע מזה.', 'אשכרה')]
        },
        {
            'id': '008', 'title': 'Zdraví a medicína', 'heb': 'בריאות ורפואה', 'tag_topic': 'zdraví',
            'article': 'כאשר מרגישים לא טוב, חשוב לקבוע תור לרופא בקופת החולים. הרופא מבצע בדיקה מקיפה כדי לאבחן את המחלה. אם יש כאב או דלקת, הרופא יכול לתת מרשם לתרופה מתאימה. במקרה של רגישות לתרופות, יש לעדכן את הצוות. לאחר הטיפול, מתחיל תהליך ההחלמה. חשוב להקשיב לגוף כדי לחזור לאיתנו.',
            'vocab': [
                ('טיפול', 'ט.פ.ל', 'tipul', 'léčba / péče', 'טיפול רפואי', 'podst_jméno'),
                ('בדיקה', 'ב.ד.ק', 'bdika', 'kontrola / test', 'בדיקת דם', 'podst_jméno'),
                ('תרופה', 'ר.פ.א', 'trufa', 'lék', 'לקחת תרופה', 'podst_jméno'),
                ('מרשם', 'ר.ש.ם', 'miršam', 'recept', 'מרשם מהרופא', 'podst_jméno'),
                ('מחלה', 'ח.ל.ה', 'machala', 'nemoc', 'מחלה קשה', 'podst_jméno'),
                ('החלמה', 'ח.ל.ם', 'hachlama', 'zotavení', 'החלמה מהירה', 'podst_jméno'),
                ('כאב', 'כ.א.ב', 'ke\'ev', 'bolest', 'כאב ראש', 'podst_jméno'),
                ('רגישות', 'ר.ג.ש', 'regišut', 'citlivost / alergie', 'רגישות לפניצילין', 'podst_jméno'),
                ('דלקת', 'ד.ל.ק', 'daleket', 'zánět', 'דלקת גרון', 'podst_jméno'),
                ('אבחנה', 'ב.ח.ן', 'abchana', 'diagnóza', 'אבחנה מדויקת', 'podst_jméno')
            ],
            'grammar': '<p>Kořen <strong>ר.פ.א</strong> (léčit) tvoří celou rodinu slov: <em>rofe</em> (lékař), <em>trufa</em> (lék), <em>refua</em> (medicína).</p><p>Slovo <strong>דלקת</strong> (daleket - zánět) souvisí s kořenem <strong>ד.ל.ק</strong> (hořet, zapálit), což přesně popisuje pocit při zánětu.</p>',
            'exercise': [('קיבלתי _______ לתרופה חדשה.', 'מרשם'), ('הוא סובל מ_______ גרון.', 'דלקת'), ('הרופא ביצע _______ מקיפה.', 'בדיקה')]
        },
        {
            'id': '009', 'title': 'Příroda a cestování', 'heb': 'טבע וטיולים', 'tag_topic': 'příroda',
            'article': 'הטבע בישראל מגוון מאוד, מהחרמון בצפון ועד אילת בדרום. ישראלים רבים אוהבים לצאת לטיולים בשמורות טבע וללכת במסלולים מאתגרים. הנוף מהרי הגולן או מהרי אילת עוצר נשימה. חשוב מאוד לשמור על הסביבה ולמנוע זיהום כדי להגן על חיות הבר. מדריך טיולים מנוסה יכול להוסיף ידע רב על ההיסטוריה והגיאולוגיה.',
            'vocab': [
                ('נוף', 'נ.ו.ף', 'nof', 'výhled / krajina', 'נוף מרהיב', 'podst_jméno'),
                ('מסלול', 'ס.ל.ל', 'maslul', 'trasa / cesta', 'מסלול הליכה', 'podst_jméno'),
                ('שמורה', 'ש.מ.ר', 'šmura', 'rezervace', 'שמורת טבע', 'podst_jméno'),
                ('סביבה', 'ס.ב.ב', 'sviva', 'prostředí', 'איכות הסביבה', 'podst_jméno'),
                ('זיהום', 'ז.ה.ם', 'zihum', 'znečištění', 'זיהום אוויר', 'podst_jméno'),
                ('שימור', 'ש.מ.ר', 'šimur', 'ochrana / konzervace', 'שימור הטבע', 'podst_jméno'),
                ('חופש', 'ח.פ.ש', 'chofeš', 'svoboda / volno', 'לצאת לחופש', 'podst_jméno'),
                ('הרפתקה', '---', 'harpatka', 'dobrodružství', 'הרפתקה גדולה', 'podst_jméno'),
                ('אתר', '---', 'atar', 'místo / památka', 'אתר מורשת', 'podst_jméno'),
                ('מדריך', 'ד.ר.ך', 'madrich', 'průvodce', 'מדריך טיולים', 'podst_jméno')
            ],
            'grammar': '<p>Předpona <strong>מ</strong> se často používá k vytvoření místa (makom) nebo nástroje/osoby. <strong>מדריך</strong> (madrich) je ten, kdo ukazuje cestu (derech).</p><p>Slovo <strong>שמורה</strong> (šmura - rezervace) pochází z kořene <strong>ש.מ.ר</strong> (střežit, hlídat).</p>',
            'exercise': [('טיילנו ב_______ טבע יפה.', 'שמורת'), ('ה_______ מהר חרמון מדהים.', 'נוף'), ('צריך למנוע _______ בסביבה.', 'זיהום')]
        },
        {
            'id': '010', 'title': 'Vzdělání a věda', 'heb': 'חינוך ומדע', 'tag_topic': 'věda',
            'article': 'השכלה היא המפתח להצלחה בעידן המודרני. אוניברסיטאות בישראל נחשבות למוסדות מחקר מובילים בעולם. סטודנטים רבים לומדים לתואר ראשון ושני ומפתחים מיומנויות חדשות. הממשלה מעניקה מלגות לסטודנטים מצטיינים כדי לעודד למידה וגילויים מדעיים. כל שיעור באוניברסיטה מרחיב את הידע והתפתחות.',
            'vocab': [
                ('מחקר', 'ח.ק.ר', 'mechkar', 'výzkum', 'מחקר מדעי', 'podst_jméno'),
                ('השכלה', 'ש.כ.ל', 'haskala', 'vzdělání', 'השכלה גבוהה', 'podst_jméno'),
                ('מיומנות', 'י.מ.נ', 'mejummanut', 'dovednost', 'מיומנויות למידה', 'podst_jméno'),
                ('שיעור', 'ש.ע.ר', 'ši\'ur', 'lekce / hodina', 'שיעור עברית', 'podst_jméno'),
                ('מלגה', 'מ.ל.ג', 'milga', 'stipendium', 'קיבלתי מלגה', 'podst_jméno'),
                ('מוסד', 'י.ס.ד', 'mosad', 'instituce / ústav', 'מוסד אקדמי', 'podst_jméno'),
                ('תואר', 'ת.א.ר', 'to\'ar', 'titul (akademický)', 'תואר ראשון', 'podst_jméno'),
                ('ידע', 'י.ד.ע', 'jeda', 'znalosti / vědění', 'ידע רב', 'podst_jméno'),
                ('למידה', 'ל.מ.ד', 'lemida', 'učení se (proces)', 'שיטות למידה', 'podst_jméno'),
                ('גילוי', 'ג.ל.ה', 'giluj', 'objev', 'גילוי חדש', 'podst_jméno')
            ],
            'grammar': '<p>Kořen <strong>י.ד.ע</strong> (vědět) tvoří slova: <em>jeda</em> (znalost), <em>muda\'ut</em> (povědomí), <em>mada</em> (věda).</p><p>Slovo <strong>השכלה</strong> (haskala - vzdělání) souvisí s intelektem (sechel). V 18. a 19. století se tak nazývalo židovské osvícenství.</p>',
            'exercise': [('הוא לומד לתואר _______ באוניברסיטה.', 'שני'), ('קיבלתי _______ למימון הלימודים.', 'מלגה'), ('האוניברסיטה היא _______ מחקר חשוב.', 'מוסד')]
        },
        {
            'id': '011', 'title': 'Izraelská společnost', 'heb': 'חברה ודמוגרפיה', 'tag_topic': 'společnost',
            'article': 'החברה הישראלית מתאפיינת במגוון רחב של קבוצות ומגזרים. אחד הנושאים המרכזיים הוא המתח בין דתיים לחילונים. בשנים האחרונות גדלה המודעות לשילוב הציבור החרדי בשוק התעסוקה ובצה"ל. בנוסף, ישראל ממשיכה לקלוט עולים חדשים מרחבי העולם. כל מגזר שואף לשמור על הזהות הייחודית שלו, אך קיימת שאיפה לאחדות לאומית וסובלנות הדדית.',
            'vocab': [
                ('מגזר', 'ג.ז.ר', 'migzar', 'sektor / odvětví', 'המגזר החרדי', 'podst_jméno'),
                ('חילוני', 'ח.ל.נ', 'chiloni', 'sekulární', 'בית ספר חילוני', 'příd_jméno'),
                ('דתי', 'ד.ת', 'dati', 'náboženský', 'משפחה דתית', 'příd_jméno'),
                ('חרדי', 'ח.ר.ד', 'charedi', 'ultraortodoxní', 'הציבור החרדי', 'příd_jméno'),
                ('זהות', 'ז.ה.ה', 'zehut', 'identita', 'זהות לאומית', 'podst_jméno'),
                ('עולה חדש', 'ע.ל.ה', 'ole chadaš', 'nový přistěhovalec', 'קליטת עולים חדשים', 'podst_jméno'),
                ('סובלנות', 'ס.ב.ל', 'sovlanut', 'tolerance', 'סובלנות הדדית', 'podst_jméno'),
                ('הדדי', 'ה.ד.ד', 'hadadi', 'vzájemný', 'כבוד הדדי', 'příd_jméno'),
                ('קליטה', 'ק.ל.ט', 'klita', 'přijetí / absorpce', 'מרכז קליטה', 'podst_jméno'),
                ('מתח', 'מ.ת.ח', 'metach', 'napětí / stres', 'מתח חברתי גבוה', 'podst_jméno')
            ],
            'grammar': '<p>Kořen <strong>ס.ב.ל</strong> znamená „nést břemeno“. <strong>סובלנות</strong> (sovlanut - tolerance) je schopnost unést odlišnost druhého, zatímco <strong>סבלנות</strong> (savlanut - trpělivost) je schopnost nést břemeno času.</p><p>Slovo <strong>מגזר</strong> (migzar - sektor) souvisí s řezáním nebo vymezováním (gezer).</p>',
            'exercise': [('חשוב לגלות _______ כלפי האחר.', 'סובלנות'), ('הוא הגיע לישראל כ_______.', 'עולה חדש'), ('יש _______ גבוה בין הקבוצות.', 'מתח')]
        },
        {
            'id': '012', 'title': 'Život a práce v Izraeli', 'heb': 'חיים ועבודה בישראל', 'tag_topic': 'práce',
            'article': 'החיים בישראל משלבים בין עבודה אינטנסיבית לבין דגש חזק על משפחה ופנאי. מושג ה"וורק-לייף באלאנס" הופך ליותר פופולרי, אך עדיין ישראלים רבים עובדים שעות נוספות. שירות המילואים משפיע על שוק העבודה ועל החיים האישיים. בתקופות של חופש, הישראלים אוהבים לטייל או לטוס לחו"ל. למרות הלחץ, קיימת תחושה של ערבות הדדית וסיוע בעת צרה.',
            'vocab': [
                ('פנאי', 'פ.נ.י', 'pnaj', 'volný čas', 'תרבות הפנאי', 'podst_jméno'),
                ('שעות נוספות', 'י.ס.ף', 'ša\'ot nosafot', 'přesčasy', 'לעבוד שעות נוספות', 'fráze'),
                ('מילואים', 'מ.ל.א', 'miluim', 'vojenská záloha', 'שירות מילואים פעיל', 'podst_jméno'),
                ('חופש', 'ח.פ.ש', 'chofeš', 'dovolená / svoboda', 'לצאת לחופש שנתי', 'podst_jméno'),
                ('חו"ל', '---', 'chul', 'zahraničí', 'לטוס לחו"ל בקיץ', 'podst_jméno'),
                ('ערבות', 'ע.ר.ב', 'aravut', 'záruka / ručení', 'ערבות הדדית', 'podst_jméno'),
                ('צרה', 'צ.ר.ר', 'cara', 'potíž / neštěstí', 'חבר בעת צרה', 'podst_jméno'),
                ('אתגר', 'ת.ג.ר', 'etgar', 'výzva', 'אתגר מקצועי חדש', 'podst_jméno'),
                ('שגרה', 'ש.ג.ר', 'šigra', 'rutina', 'לחזור לשגרה', 'podst_jméno'),
                ('איזון', 'א.ז.נ', 'izun', 'rovnováha / balans', 'איזון בין עבודה לבית', 'podst_jméno')
            ],
            'grammar': '<p>Kořen <strong>מ.ל.א</strong> znamená „plný“ nebo „naplnit“. <strong>מילואים</strong> (miluim - záloha) původně znamenalo „doplnění“ nebo „výplň“ armády.</p><p>Slovo <strong>שגרה</strong> (šigra - rutina) souvisí s posíláním nebo plynulým tokem (š-g-r).</p>',
            'exercise': [('הוא נקרא לשירות _______.', 'מילואים'), ('צריך למצוא _______ בין עבודה למשפחה.', 'איזון'), ('הם טסים ל_______ בקיץ.', 'חו"ל')]
        },
        {
            'id': '013', 'title': 'Kultura a svátky', 'heb': 'תרבות וחגים לאומיים', 'tag_topic': 'kultura',
            'article': 'התרבות הישראלית היא פסיפס מרתק של מסורת יהודית ומודרניות מערבית. החגים הלאומיים, כמו יום העצמאות ויום הזיכרון, ממלאים תפקיד מרכזי. ביום העצמאות נהוג לערוך פיקניקים ולצפות במטס של חיל האוויר, בעוד שביום הזיכרון שוררת אווירה של הזכרה עם הנופלים. מוזיקה ישראלית משקפת את הגעגועים והתקוות של החברה.',
            'vocab': [
                ('תרבות', 'ר.ב.ה', 'tarbut', 'kultura', 'תרבות ישראלית', 'podst_jméno'),
                ('פסיפס', '---', 'psifas', 'mozaika', 'פסיפס מרתק', 'podst_jméno'),
                ('מסורת', 'מ.ס.ר', 'masoret', 'tradice', 'מסורת יהודית', 'podst_jméno'),
                ('לאומי', 'ל.א.ם', 'le\'umi', 'národní', 'חגים לאומיים', 'příd_jméno'),
                ('עצמאות', 'ע.צ.ם', 'acma\'ut', 'nezávislost', 'יום העצמאות', 'podst_jméno'),
                ('זיכרון', 'ז.כ.ר', 'zikaron', 'paměť / vzpomínka', 'יום הזיכרון', 'podst_jméno'),
                ('מטס', 'ט.ו.ס', 'matas', 'letecká přehlídka', 'מטס חיל האוויר', 'podst_jméno'),
                ('הזכרה', 'ז.כ.ר', 'hazkara', 'vzpomínkový obřad / pieta', 'טקס הזכרה', 'podst_jméno'),
                ('געגוע', 'ג.ע.ג.ע', 'ga\'agua', 'stesk / touha', 'געגועים ותקוות', 'podst_jméno'),
                ('תקווה', 'ק.ו.ה', 'tikva', 'naděje', 'התקווה היא ההמנון', 'podst_jméno')
            ],
            'grammar': '<p>Vazba <strong>smichut</strong> je klíčová pro názvy svátků (Jom ha-Acma\'ut). Kořen <strong>ר.ב.ה</strong> (množit se) tvoří slovo <strong>תרבות</strong> (tarbut - to, co se pěstuje/rozvíjí).</p><p>Slovo <strong>פסיפס</strong> (psifas - mozaika) je přejímka z řeckého <em>psēphos</em> (kamínek).</p>',
            'exercise': [('ביום העצמאות יש _______ של חיל האוויר.', 'מטס'), ('החברה הישראלית היא _______ של תרבויות.', 'פסיפס'), ('אנחנו הולכים לטקס _______.', 'הזכרה')]
        },
        {
            'id': '014', 'title': 'Válka a bezpečnost', 'heb': 'מלחמה וביטחון', 'tag_topic': 'válka',
            'article': 'המצב הביטחוני בישראל דורש ערנות מתמדת. צה"ל פועל להגנת הגבולות והעורף מפני איומים. במהלך אזעקה, התושבים נכנסים למרחבים מוגנים בזמן שכיפת ברזל מיירטת טילים. החוסן הלאומי נמדד ביכולת של החברה להמשיך בשגרה גם בזמן מלחמה בחזית.',
            'vocab': [
                ('מלחמה', 'מ.ל.ח.מ', 'milchama', 'válka', 'מלחמה בחזית', 'podst_jméno'),
                ('ביטחון', 'ב.ט.ח', 'bitachon', 'bezpečnost', 'המצב הביטחוני', 'podst_jméno'),
                ('צה"ל', '---', 'cahal', 'Izraelské obranné síly', 'שירות בצה"ל', 'podst_jméno'),
                ('כיפת ברזל', '---', 'kipat barzel', 'Železná kopule', 'מערכת כיפת ברזל', 'fráze'),
                ('אזעקה', 'ז.ע.ק', 'az\'aka', 'siréna / poplach', 'נשמעה אזעקה', 'podst_jméno'),
                ('חוסן', 'ח.ס.נ', 'chosen', 'odolnost / resilience', 'חוסן לאומי', 'podst_jméno'),
                ('איום', 'א.י.מ', 'ijum', 'hrozba', 'איום קיומי', 'podst_jméno'),
                ('להגן', 'ג.נ.נ', 'lehagen', 'bránit', 'להגן על העורף', 'sloveso'),
                ('חזית', 'ח.ז.ת', 'chazit', 'fronta', 'חיילים בחזית', 'podst_jméno'),
                ('עורף', 'ע.ר.פ', 'oref', 'zázemí / týl', 'הגנת העורף', 'podst_jméno')
            ],
            'grammar': '<p>Slovo <strong>מלחמה</strong> (milchama - válka) má stejný kořen jako <em>lechem</em> (chleba). Etymologicky to naznačuje boj o základní zdroje.</p><p>Zkratka <strong>צה"ל</strong> (Cahal) znamená Cva Hagana le-Jisra\'el. V hebrejštině se zkratky často vyslovují jako samostatná slova.</p>',
            'exercise': [('בזמן _______ נכנסים למרחב מוגן.', 'אזעקה'), ('מערכת _______ מיירטת טילים.', 'כיפת ברזל'), ('החיילים מגנים על ה_______.', 'חזית')]
        },
        {
            'id': '015', 'title': 'Gastronomie a jídlo', 'heb': 'אוכל ומטבח', 'tag_topic': 'jídlo',
            'article': 'המטבח הישראלי ידוע בטעמים עזים ושימוש רב בתבלינים טריים. אירוח ישראלי טיפוסי כולל שולחן מלא בסלטים, חומוס ופיתות חמות. כל בשלן גאה במתכון האישי שלו למנה האהובה. הארוחה היא זמן לבילוי משפחתי, והאוכל תמיד טעים ומזמין.',
            'vocab': [
                ('חומוס', '---', 'chumus', 'hummus', 'חומוס טעים מאוד', 'podst_jméno'),
                ('פיתה', '---', 'pita', 'pita', 'פיתה חמה מהתנור', 'podst_jméno'),
                ('תבלין', 'ב.ל.נ', 'tavlin', 'koření', 'תבלינים מהשוק', 'podst_jméno'),
                ('מטבח', 'ט.ב.ח', 'mitbach', 'kuchyně', 'מטבח ישראלי', 'podst_jméno'),
                ('אירוח', 'ר.ו.ח', 'iruach', 'pohostinnost', 'מנהגי אירוח', 'podst_jméno'),
                ('טעים', 'ט.ע.מ', 'ta\'im', 'chutný', 'אוכל טעים', 'příd_jméno'),
                ('בשלן', 'ב.ש.ל', 'bašlan', 'kuchař', 'הוא בשלן מצוין', 'podst_jméno'),
                ('מתכון', 'כ.ו.נ', 'matkon', 'recept', 'מתכון סודי', 'podst_jméno'),
                ('טרי', 'ט.ר.י', 'tari', 'čerstvý', 'ירקות טריים', 'příd_jméno'),
                ('ארוחה', 'א.ר.ח', 'arucha', 'jídlo / chod', 'ארוחת ערב', 'podst_jméno')
            ],
            'grammar': '<p>Kořen <strong>ט.ע.מ</strong> tvoří slova <em>ta\'im</em> (chutný) i <em>ta\'am</em> (chuť/význam). </p><p>Slovo <strong>ארוחה</strong> (arucha) souvisí s hosty (orchim), kteří k jídlu přicházejí.</p>',
            'exercise': [('קניתי _______ טריים בשוק.', 'תבלינים'), ('האוכל במסעדה היה מאוד _______.', 'טעים'), ('יש לי _______ חדש לעוגה.', 'מתכון')]
        },
        {
            'id': '016', 'title': 'Historie a Jeruzalém', 'heb': 'היסטוריה וירושלים', 'tag_topic': 'historie',
            'article': 'ירושלים היא עיר עם היסטוריה עתיקה ומורכבת. בלב העיר העתיקה נמצא הכותל המערבי, אתר קדוש ליהודים מכל העולם. חומות העיר מספרות סיפורים על תקופות שונות ועל ארכיאולוגיה מרתקת. תפילה בבית המקדש או במסגד מסמלת את החשיבות הרוחנית, והשאיפה היא תמיד לדו-קיום בשלום.',
            'vocab': [
                ('עיר עתיקה', '---', 'ir atika', 'Staré Město', 'טיול בעיר העתיקה', 'fráze'),
                ('הכותל המערבי', '---', 'hakotel hama\'aravi', 'Zeď nářků', 'תפילה בכותל', 'fráze'),
                ('ארכיאולוגיה', '---', 'archeologija', 'archeologie', 'חפירות ארכיאולוגיות', 'podst_jméno'),
                ('קדוש', 'ק.ד.ש', 'kadoš', 'svatý', 'מקום קדוש', 'příd_jméno'),
                ('אתר', '---', 'atar', 'místo / lokalita', 'אתר מורשת עולמי', 'podst_jméno'),
                ('חומות', 'ח.ו.מ', 'chomot', 'hradby', 'חומות ירושלים', 'podst_jméno'),
                ('דו-קיום', '---', 'du-kijum', 'koexistence', 'דו-קיום בירושלים', 'podst_jméno'),
                ('היסטוריה', '---', 'istorija', 'historie', 'שיעור היסטוריה', 'podst_jméno'),
                ('מקדש', 'ק.ד.ש', 'mikdaš', 'chrám', 'בית המקדש', 'podst_jméno'),
                ('תפילה', 'פ.ל.ל', 'tfila', 'modlitba', 'סידור תפילה', 'podst_jméno')
            ],
            'grammar': '<p>Kořen <strong>ק.ד.ש</strong> (svatý) je základem pro <em>kadoš</em>, <em>mikdaš</em> (chrám) i <em>kiduš</em>. </p><p>Slovo <strong>חומות</strong> (chomot) je množné číslo od <em>choma</em> (hradba), což se liší od slova <em>kir</em> (obyčejná zeď).</p>',
            'exercise': [('העיר ה_______ היא מרכז ירושלים.', 'עתיקה'), ('הכותל הוא _______ קדוש.', 'אתר'), ('אנחנו מקווים ל_______ בעיר.', 'דו-קיום')]
        },
        {
            'id': '017', 'title': 'Moderní Tel Aviv', 'heb': 'תל אביב המודרנית', 'tag_topic': 'město',
            'article': 'תל אביב היא "עיר ללא הפסקה", הידועה באווירה תוססת ובתרבות עשירה. חוף הים מלא באנשים בכל ימות השנה, וגורדי שחקים חדשים משנים את קו הרקיע. העיר היא מרכז עולמי של סטארט-אפים ובילויים במועדונים. רבים רוכבים על אופניים כדי להגיע לשוק ולטעום מהתוצרת המקומית.',
            'vocab': [
                ('חוף ים', '---', 'chof jam', 'pláž', 'ללכת לחוף הים', 'fráze'),
                ('מועדון', 'ו.ע.ד', 'moadon', 'klub', 'ריקודים במועדון', 'podst_jméno'),
                ('סטארט-אפ', '---', 'start-ap', 'startup', 'חברת סטארט-אפ', 'podst_jméno'),
                ('ללא הפסקה', '---', 'lelo hafsaka', 'bez přestávky', 'עיר ללא הפסקה', 'fráze'),
                ('בילוי', 'ב.ל.ה', 'biluj', 'zábava', 'מקום בילוי', 'podst_jméno'),
                ('גורד שחקים', '---', 'gored schakim', 'mrakodrap', 'גורדי שחקים בתל אביב', 'podst_jméno'),
                ('תוסס', 'ת.ס.ס', 'toses', 'živý / pulzující', 'חיים תוססים', 'příd_jméno'),
                ('תרבות', 'ר.ב.ה', 'tarbut', 'kultura', 'חיי תרבות', 'podst_jméno'),
                ('אופניים', '---', 'ofanajim', 'jízdní kolo', 'לרכוב על אופניים', 'podst_jméno'),
                ('שוק', '---', 'šuk', 'trh', 'לקנות פירות בשוק', 'podst_jméno')
            ],
            'grammar': '<p>Výraz <strong>גורד שחקים</strong> doslova znamená „škrábač nebes“ (shakim - nebesa). </p><p>Slovo <strong>תוסס</strong> (toses) se používá jak pro bublinkové nápoje, tak pro živou atmosféru.</p>',
            'exercise': [('תל אביב היא עיר ללא _______.', 'הפסקה'), ('יש _______ רבים במרכז העיר.', 'גורדי שחקים'), ('אני אוהב ללכת ל_______ הים.', 'חוף')]
        },
        {
            'id': '018', 'title': 'Příroda a Počasí', 'heb': 'טבע ומזג אוויר', 'tag_topic': 'příroda',
            'article': 'מזג האוויר בישראל משתנה בין עונה לעונה. בקיץ שורר שרב כבד עם לחות גבוהה במישור החוף, בעוד שבחורף הגשם מביא ברכה לחקלאות. הטבע מציע ניגודים: מהמדבר השקט וים המלח הנמוך בעולם, ועד לשלג בחרמון. הרוח והשמש משפיעים על החיים ועל מצב הרוח של התושבים.',
            'vocab': [
                ('מדבר', 'ד.ב.ר', 'midbar', 'poušť', 'טיול בממדר', 'podst_jméno'),
                ('ים המלח', '---', 'jam hamelach', 'Mrtvé moře', 'לצוף בים המלח', 'fráze'),
                ('גשם', 'ג.ש.מ', 'gešem', 'déšť', 'גשם ראשון', 'podst_jméno'),
                ('שרב', 'ש.ר.ב', 'šarav', 'horko / veda', 'יום שרב כבד', 'podst_jméno'),
                ('עונה', '---', 'ona', 'roční období', 'עונת המעבר', 'podst_jméno'),
                ('לחות', 'ל.ח.ת', 'lachut', 'vlhkost', 'לחות גבוהה', 'podst_jméno'),
                ('שלג', 'ש.ל.ג', 'šeleg', 'sníh', 'שלג בחרמון', 'podst_jméno'),
                ('רוח', 'ר.ו.ח', 'ruach', 'vítr', 'רוח חזקה', 'podst_jméno'),
                ('חקלאות', 'ח.ק.ל', 'chakla\'ut', 'zemědělství', 'פיתוח החקלאות', 'podst_jméno'),
                ('שמש', 'ש.מ.ש', 'šemeš', 'slunce', 'שמש חזקה', 'podst_jméno')
            ],
            'grammar': '<p>Kořen <strong>ד.ב.ר</strong> (mluvit) tvoří slovo <em>midbar</em> (poušť), snad jako místo, kde k člověku mluví Bůh nebo kde je slyšet ticho. </p><p>Slovo <strong>שרב</strong> (šarav) označuje specifické suché a horké počasí z pouště.</p>',
            'exercise': [('בקיץ יש _______ כבד.', 'שרב'), ('ה_______ ירד כל הלילה.', 'גשם'), ('אנחנו נוסעים ל_______ המלח.', 'ים')]
        },
        {
            'id': '019', 'title': 'Doprava a infrastruktura', 'heb': 'תחבורה ותשתית', 'tag_topic': 'doprava',
            'article': 'התשתית בישראל מתפתחת במהירות כדי להתמודד עם העומס בכבישים. נסיעה ברכבת הפכה ליעילה יותר, אך רבים עדיין משתמשים באוטובוס או ברכב פרטי. פקק תנועה בשעות הבוקר הוא מחזה נפוץ בדרך לנמל התעופה. כל נתיב חדש ותחנה מודרנית עוזרים לשפר את זרימת התחבורה.',
            'vocab': [
                ('רכבת', 'ר.כ.ב', 'rakevet', 'vlak', 'נסיעה ברכבת', 'podst_jméno'),
                ('אוטובוס', '---', 'otobus', 'autobus', 'תחנת אוטובוס', 'podst_jméno'),
                ('פקק', 'פ.ק.ק', 'pkak', 'dopravní zácpa', 'פקק בכביש 1', 'podst_jméno'),
                ('נמל תעופה', '---', 'nemal teufa', 'letište', 'נמל תעופה בן גוריון', 'podst_jméno'),
                ('נסיעה', 'נ.ס.ע', 'nesia', 'jízda / cesta', 'נסיעה טובה', 'podst_jméno'),
                ('נתיב', 'נ.ת.ב', 'nativ', 'pruh / trasa', 'נתיב תחבורה ציבורית', 'podst_jméno'),
                ('רכב', 'ר.כ.ב', 'rechev', 'vozidlo', 'רכב חשמלי', 'podst_jméno'),
                ('כביש', 'כ.ב.ש', 'kviš', 'silnice', 'כביש מהיר', 'podst_jméno'),
                ('תחנה', 'ח.נ.ה', 'tachana', 'stanice', 'תחנה מרכזית', 'podst_jméno'),
                ('עומס', 'ע.ו.מ.ס', 'omes', 'zátěž / přetížení', 'עומס בכבישים', 'podst_jméno')
            ],
            'grammar': '<p>Kořen <strong>ר.כ.ב</strong> (jet/vézt se) tvoří <em>rechev</em> (vůz), <em>rakevet</em> (vlak) i <em>rochav</em> (jezdec). </p><p>Slovo <strong>פקק</strong> (pkak) původně znamená „zátka“, což výstižně popisuje ucpanou silnici.</p>',
            'exercise': [('ה_______ איחרה בגלל תקלה.', 'רכבת'), ('יש _______ כבד בדרך לתל אביב.', 'פקק'), ('הגענו ל_______ התעופה בזמן.', 'נמל')]
        },
        {
            'id': '020', 'title': 'Izraelská rodina a sny', 'heb': 'משפחה וחלומות', 'tag_topic': 'rodina',
            'article': 'המשפחה היא הלב של החברה הישראלית, במיוחד סביב ארוחת ערב של שבת. לכל אחד יש חלום על עתיד טוב יותר ועל שלום באזור. הקשר בין הדורות נבנה דרך ילדות משותפת ושירות צבא משמעותי. התקווה היא הכוח שמניע אותנו להמשיך וליצור חיים טובים יותר לכולם.',
            'vocab': [
                ('שבת', 'ש.ב.ת', 'šabat', 'šabat', 'שבת שלום', 'podst_jméno'),
                ('ארוחת ערב', '---', 'aruchat erev', 'večeře', 'ארוחת ערב משפחתית', 'fráze'),
                ('צבא', 'צ.ב.א', 'cava', 'armáda', 'שירות בצבא', 'podst_jméno'),
                ('שלום', 'ש.ל.מ', 'šalom', 'mír / pokoj', 'שלום עכשיו', 'podst_jméno'),
                ('חלום', 'ח.ל.מ', 'chalom', 'sen', 'יש לי חלום', 'podst_jméno'),
                ('משפחה', 'ש.פ.ח', 'mišpacha', 'rodina', 'משפחה חמה', 'podst_jméno'),
                ('ילדות', 'י.ל.ד', 'jaldut', 'dětství', 'זיכרון ילדות', 'podst_jméno'),
                ('תקווה', 'ק.ו.ה', 'tikva', 'naděje', 'התקווה לשלום', 'podst_jméno'),
                ('קשר', 'ק.ש.ר', 'kešer', 'spojení / vztah', 'קשר הדוק', 'podst_jméno'),
                ('עתיד', '---', 'atid', 'budoucnost', 'עתיד ורוד', 'podst_jméno')
            ],
            'grammar': '<p>Kořen <strong>ש.ב.ת</strong> znamená „přestat“ nebo „odpočívat“. Od něj je odvozen <em>šabat</em> i sloveso <em>lišbot</em> (stávkovat). </p><p>Slovo <strong>שלום</strong> (šalom) souvisí s celistvostí a úplností (šalem).</p>',
            'exercise': [('אנחנו אוכלים _______ בשבת.', 'ארוחת ערב'), ('לכל אדם יש _______ גדול.', 'חלום'), ('ה_______ היא המנון המדינה.', 'תקווה')]
        }
    ]

    for lesson in lessons:
        l_id = lesson['id']
        l_num = int(l_id)
        
        # HTML Sidebar
        html_sidebar = '<div class="sidebar"><div class="sidebar-nav"><h2>Obsah</h2>'
        for link, name in sidebar_links:
            active = ' class="active"' if link == f'lekce{l_id}.html' else ''
            html_sidebar += f'<a href="{link}"{active}>{name}</a>'
        html_sidebar += '</div><div class="resizer"></div></div>'

        # HTML Content
        html = f"""<!DOCTYPE html>
        <html lang="cs">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="style.css?v={version}">
        <title>Lekce {l_num}</title>
        <script>
            (function() {{
                const sw = localStorage.getItem('sidebarWidth');
                if (sw) {{
                    document.documentElement.style.setProperty('--sidebar-width', sw + 'px');
                }}
            }})();
        </script>
        </head>
        <body>
        {html_sidebar}
        <div class="content">

        <div class="main-header">
            <h1>Lekce {l_num}<br>{lesson['title']}</h1>
            <div class="heb-title">({lesson['heb']})</div>
        </div>
        <h3>1. Článek</h3>
        <div class="article-rtl">{lesson['article']}</div>
        <h3>2. Slovíčka</h3>
        <table dir="ltr">
            <thead><tr><th>Hebrejsky</th><th>Kořen</th><th>Výslovnost</th><th>Význam</th><th>Příklad</th></tr></thead>
            <tbody>"""
        for v in lesson['vocab']:
            html += f"<tr><td class='heb-word' dir='rtl'>{v[0]}</td><td class='root-col'>{v[1]}</td><td class='pronun-col'>{v[2]}</td><td class='meaning-col'>{v[3]}</td><td class='example-rtl' dir='rtl'>{v[4]}</td></tr>"
        
        html += f"""</tbody></table>
        <h3>3. Gramatický výklad</h3>
        <div class="grammar-box">{lesson['grammar']}</div>
        <h3>4. Cvičení</h3>
        <div class="grammar-box" style="background-color: #f9f9f9; border-right-color: #2ecc71;"><ol>"""
        for ex in lesson['exercise']:
            html += f"<li>{ex[0]}</li>"
        html += f"""</ol></div>
        <h3>5. Slovíčka pro Anki</h3>
        <div class="anki-preview">#Slovíčko;Kořen;Výslovnost;Význam;Příklad;Tag\n"""
        for v in lesson['vocab']:
            tag = f"{v[5]} {lesson['tag_topic']} lekce{l_id}"
            html += f"{v[0]};{v[1]};{v[2]};{v[3]};{v[4]};{tag}\n"
        html += f"""</div>
        <h3>6. Řešení cvičení</h3>
        <div class="grammar-box" style="background-color: #f0fff4; border-right-color: #27ae60;">
            <details><summary>Klikněte pro zobrazení</summary><ol>"""
        for ex in lesson['exercise']:
            html += f"<li>{ex[1]}</li>"
        html += """</ol></details></div><script src="script.js"></script></div></body></html>"""
        
        with open(f'lekce{l_id}.html', 'w', encoding='utf-8') as f:
            f.write(html)

        # CSV (Anki)
        csv_data = "#Slovíčko;Kořen;Výslovnost;Význam;Příklad;Tag\n"
        for v in lesson['vocab']:
            tag = f"{v[5]} {lesson['tag_topic']} lekce{l_id}"
            csv_data += f"{v[0]};{v[1]};{v[2]};{v[3]};{v[4]};{tag}\n"
        with open(f'anki_lekce{l_id}.csv', 'w', encoding='utf-8-sig') as f:
            f.write(csv_data)

        # Markdown
        md = f"# Lekce {l_num}: {lesson['title']}\n\n{md_nav}\n\n## 1. Článek\n{lesson['article']}\n\n## 2. Slovíčka\n| Hebrejsky | Kořen | Výslovnost | Význam | Příklad |\n|---|---|---|---|---|\n"
        for v in lesson['vocab']:
            md += f"| {v[0]} | {v[1]} | {v[2]} | {v[3]} | {v[4]} |\n"
        md += f"\n## 3. Gramatika\n{lesson['grammar']}\n\n## 4. Cvičení\n"
        for ex in lesson['exercise']:
            md += f"1. {ex[0]}\n"
        md += f"\n## 5. Anki náhled\n```text\n#Slovíčko;Kořen;Výslovnost;Význam;Příklad;Tag\n"
        for v in lesson['vocab']:
            tag = f"{v[5]} {lesson['tag_topic']} lekce{l_id}"
            md += f"{v[0]};{v[1]};{v[2]};{v[3]};{v[4]};{tag}\n"
        md += f"```\n\n## 6. Řešení\n"
        for ex in lesson['exercise']:
            md += f"* {ex[1]}\n"
        
        with open(f'lekce{l_id}.md', 'w', encoding='utf-8') as f:
            f.write(md)

    # Update index.html sidebar
    index_sidebar = '<div class="sidebar"><div class="sidebar-nav"><h2>Obsah</h2>'
    for link, name in sidebar_links:
        active = ' class="active"' if link == 'index.html' else ''
        index_sidebar += f'<a href="{link}"{active}>{name}</a>'
    index_sidebar += '</div><div class="resizer"></div></div>'

    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We will reconstruct index.html to be absolutely clean
    new_index = f"""<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css?v={version}">
    <title>Ivrit: Další krok - Úvod</title>
    <script>
        (function() {{
            const sw = localStorage.getItem('sidebarWidth');
            if (sw) {{
                document.documentElement.style.setProperty('--sidebar-width', sw + 'px');
                // Force immediate re-layout for some browsers
                document.documentElement.setAttribute('data-sidebar-set', 'true');
            }}
        }})();
    </script>
</head>
<body>
    {index_sidebar}
    <div class="content">
        <div class="main-header">
            <h1>Ivrit: Další krok</h1>
            <div class="heb-title">(עברית: הצעad הבא)</div>
        </div>
        <div class="grammar-box">
            <p>Vítejte v učebnici moderní hebrejštiny pro mírně pokročilé.</p>
            <h3>O učebnici</h3>
            <ul>
                <li><strong>Cíl:</strong> Rozšíření slovní zásoby tempem 10 slovíček na lekci.</li>
                <li><strong>Témata:</strong> Články čerpají ze současnosti.</li>
            </ul>
        </div>
        <script src="script.js?v={version}"></script>
    </div>
</body>
</html>"""
            
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_index)

if __name__ == '__main__':
    generate_lessons()
    print("Všech 20 lekcí a index.html bylo úspěšně vygenerováno.")
