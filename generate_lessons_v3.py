import os

def generate_lessons():
    import time
    version = int(time.time())

    # Define sidebar links for all 20 lessons + index.html
    lesson_titles = [
        "Média a aktuality", "Technologie a high-tech", "Práce a kariéra", 
        "Psychologie a emoce", "Právo a společnost", "Kultura a volný čas",
        "Slang a idiomy", "Zdraví a medicína", "Příroda a cestování",
        "Vzdělání a věda", "Izraelská společnost", "Život a práce v Izraeli",
        "Kultura a svátky", "Válka a bezpečnost", "Gastronomie a jídlo",
        "Historie a Jeruzalém", "Moderní Tel Aviv", "Příroda a Počasí",
        "Doprava a infrastruktura", "Izraelská rodina a sny"
    ]
    sidebar_links = [('index.html', 'Úvod')] + [(f'lekce{i:03d}.html', f'Lekce {i}: {lesson_titles[i-1]}') for i in range(1, 21)]
    md_nav = ' | '.join([f'[Lekce {i}]({f"lekce{i:03d}.md"})' for i in range(1, 21)])

    lessons = [
        {
            'id': '001', 'title': 'Média a aktuality', 'heb': 'מדיה וחדשות', 'tag_topic': 'média',
            'article': 'הבוקר פורסם כי הממשלה החליטה להשקיע משאבים נוספים בשיפור התשתיות. השר הממונה ציין כי המהלך נועד לחזק את הכלכלה ולספק מקומות עבודה חדשים. התושבים מקווים כי המהלך יבוצע במהירות וישפר את איכות חייהם.',
            'vocab': [
                ('לפרסם', 'פ.ר.ס.ם', 'lefarsem', 'publikovat / zveřejnit', 'פורסם כי הממשלה החליטה', 'sloveso'),
                ('ממשלה', 'מ.ש.ל', 'memšala', 'vláda', 'הממשלה החליטה להשקיע', 'podst_jméno'),
                ('להשקיע', 'ש.ק.ع', 'lehaškia', 'investovat', 'להשקיע משאבים נוספים', 'sloveso'),
                ('משאבים', 'ש.א.ב', 'mašavim', 'zdroje', 'משאבים כלכליים', 'podst_jméno'),
                ('תשתית', 'ש.ת.ת', 'taštit', 'infrastruktura', 'שיפור התשתיות', 'podst_jméno'),
                ('ממונה', 'מ.נ.ה', 'memune', 'pověřený / odpovědný', 'השר הממונה על הפרויקט', 'příd_jméno'),
                ('מהלך', 'ה.ל.ך', 'mahalach', 'krok / proces / tah', 'המהלך נועד לחזק', 'podst_jméno'),
                ('נועד', 'י.ע.д', 'no\'ad', 'určen k / má za cíl', 'הפרויקט נועד לתושבים', 'sloveso'),
                ('כלכלה', 'כ.ל.כ.ל', 'kalkala', 'ekonomika', 'הכלכלה המקומית חזקה', 'podst_jméno'),
                ('תושב', 'י.ש.ב', 'tošav', 'obyvatel', 'התושבים גרים בצפון', 'podst_jméno')
            ],
            'grammar': '<p>V textu vidíme pasivum <strong>פורסם</strong> (pursam). Kořen <strong>מ.ש.ל</strong> souvisí s vládnutím.</p>',
            'exercise': [('הבוקר _______ כי הממשלה החליטה.', 'פורסם'), ('המהלך _______ לחזק את הכלכלה.', 'נועד'), ('השר ה_______ על הפרויקט.', 'ממונה')]
        },
        {
            'id': '002', 'title': 'Technologie a high-tech', 'heb': 'טכנולוגיה והיי-טק', 'tag_topic': 'technologie',
            'article': 'ישראל ידועה בעולם כ"אומת הסטארט-אפ". חברות ישראליות רבות מפתחות טכנולוגיה חדשנית בתחומי הבינה המלאכותית והסייבר. כל חברה מנסה למצוא פתרון לבעיה גלובלית וליצור מוצר מוצלח שישרת מיליוני משתמשים ברחבי העולם.',
            'vocab': [
                ('לפתח', 'פ.ת.ח', 'lefateach', 'vyvíjet / rozvíjet', 'לפתח טכנולוגיה חדשה', 'sloveso'),
                ('חדשני', 'ח.д.ש', 'chadašani', 'inovativní', 'מוצר חדשני ומעניין', 'příd_jméno'),
                ('תחום', 'ת.ח.מ', 'tchum', 'obor / oblast', 'בתחום הבינה המלאכותית', 'podst_jméno'),
                ('בינה מלאכותית', '---', 'bina melachutit', 'umělá inteligence', 'עתיד הבינה המלאכותית', 'podst_jméno'),
                ('חברה', 'ח.ב.ר', 'chevra', 'společnost / firma', 'חברת סטארט-אפ', 'podst_jméno'),
                ('פתרון', 'פ.ת.ר', 'pitron', 'řešení', 'למצוא פתרון לבעיה', 'podst_jméno'),
                ('מוצר', 'י.צ.ר', 'mucar', 'produkt / výrobek', 'מוצר מוצלח מאוד', 'podst_jméno'),
                ('משתמש', 'ש.מ.ש', 'mištameš', 'uživatel', 'מיליוני משתמשים בעולם', 'podst_jméno'),
                ('פיתוח', 'פ.ת.ח', 'pituach', 'vývoj', 'מרכז פיתוח גדול', 'podst_jméno'),
                ('מוצלח', 'צ.ל.ח', 'muclach', 'úspěšný', 'פרויekt מוצלח ורווחי', 'příd_jméno')
            ],
            'grammar': '<p>Slovo <strong>פיתוח</strong> je podstatné jméno slovesné od <strong>לפתח</strong>.</p>',
            'exercise': [('ישראל מפתחת _______ חדשנית.', 'טכנולוגיה'), ('החברה מצאה _______ לבעיה.', 'פתרון'), ('ה_______ בתל אביiv מוביל.', 'מרכז הפיתוח')]
        }
    ]
    # Lessons 3-20 would be here...

    for lesson in lessons:
        l_id = lesson['id']
        l_num = int(l_id)
        
        # HTML Sidebar
        html_sidebar = '<div class="sidebar"><div class="sidebar-nav"><h2>Obsah</h2>'
        for link, name in sidebar_links:
            active = ' class="active"' if link == f'lekce{l_id}.html' else ''
            html_sidebar += f'<a href="{link}"{active}>{name}</a>'
        html_sidebar += '</div></div>'

        # HTML Content
        html = f"""<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css?v={version}">
    <title>Lekce {l_num}</title>
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
        html += f"""</ol></details></div><script src="script.js?v={version}"></script></div></body></html>"""
        
        with open(f'lekce{l_id}.html', 'w', encoding='utf-8') as f:
            f.write(html)

    # Reconstruct index.html
    index_sidebar = '<div class="sidebar"><div class="sidebar-nav"><h2>Obsah</h2>'
    for link, name in sidebar_links:
        active = ' class="active"' if link == 'index.html' else ''
        index_sidebar += f'<a href="{link}"{active}>{name}</a>'
    index_sidebar += '</div></div>'

    new_index = f"""<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css?v={version}">
    <title>Ivrit: Další krok - Úvod</title>
</head>
<body>
    {index_sidebar}
    <div class="content">
        <div class="main-header">
            <h1>Ivrit: Další krok</h1>
            <div class="heb-title">(עברית: הצעד הבא)</div>
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
    print("Vše vygenerováno s pevnou šířkou sidebaru.")
