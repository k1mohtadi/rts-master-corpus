#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builds and synchronizes the RTS Master Corpus & Universal Glossary files:
1. sentence_decisions.csv & SENTENCE_DECISIONS.md
2. universal_glossary.csv & UNIVERSAL_GLOSSARY.md
3. README.md
"""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SENTENCE_DECISIONS = [
    {
        "ID": "SM-899-01",
        "Project": "Encyclopedia of Social & Political Movements (Vol. 1)",
        "Chapter_Entry": "Entry 899: Gezi Park Protests (Istanbul)",
        "English_Sentence": "Urban mobilization was, at its onset, directed toward the demolition of Gezi Park according to a plan by the Istanbul municipality, then run by the Justice and Development Party (AKP), to replace it with a commercial-touristic replica of an Ottoman military barracks, which was razed in the early years of the Turkish Republic.",
        "RTS_Version_Invalid": "بسیج شهری در آغاز متوجه تخریب پارک گزی بر طبق برنامۀ شهرداری استانبول بود (که در آن زمان زیر نظر حزب عدالت و توسعه اداره می‌شد) تا آن را با نسخۀ بدل تجاری ـ توریستیِ یک پادگان نظامی عثمانی که در سال‌های اولیۀ جمهوری ترکیه تخریب شده بود، جایگزین کند.",
        "Human_Edited_Version": "بسیج شهری در آغاز متوجه تخریب پارک گزی بر طبق برنامۀ شهرداری استانبول بود (که در آن زمان زیر نظر حزب عدالت و توسعه اداره می‌شد) تا آن را با یک نسخۀ بدل تجاری ـ توریستی از یک پادگان نظامی عثمانی جایگزین کند که در سال‌های اولیۀ جمهوری ترکیه تخریب شده بود.",
        "Error_Category": "Syntactic Extraposition (پس‌گشت بند موصولی)",
        "Editorial_Rationale": "Move the verb «جایگزین کند» before the relative clause «که در سال‌های اولیۀ جمهوری ترکیه تخریب شده بود» so the verb is not stranded at the end of a long modifier."
    },
    {
        "ID": "SM-899-02",
        "Project": "Encyclopedia of Social & Political Movements (Vol. 1)",
        "Chapter_Entry": "Entry 899: Gezi Park Protests (Istanbul)",
        "English_Sentence": "Police brutality against peaceful protesters trying to block the ongoing demolition, documented and spread virally through social media channels, sparked public outrage, and jolted masses into a large-scale anti-government uprising that lasted for weeks.",
        "RTS_Version_Invalid": "خشونت پلیس علیه معترضان آرام که تلاش می‌کردند مانع از ادامۀ تخریب شوند، مستند شد و به سرعت از طریق کانال‌های رسانه‌های اجتماعی گسترش یافت، خشم عمومی را برانگیخت و توده‌ها را در خیزش ضددولتی بزرگ‌مقیاسی تکان داد که برای هفته‌ها به طول انجامید.",
        "Human_Edited_Version": "خشونت پلیس علیه معترضانِ آرام که تلاش می‌کردند مانع از ادامۀ تخریب شوند، به شکل مستند ثبت شد و به سرعت از طریق کانال‌های رسانه‌های اجتماعی انتشار یافت. با برانگیخته شدن خشم عمومی معترضان به شکل توده‌ای در خیزش ضددولتی بزرگ‌مقیاسی شرکت کردند که چندین هفته به طول انجامید.",
        "Error_Category": "Sentence Decomposition & Calque Eradication",
        "Editorial_Rationale": "Break overloaded 4-verb sentence into two natural sentences; replace calques «مستند شد» -> «به شکل مستند ثبت شد», «توده‌ها را تکان داد» (jolted masses) -> «معترضان به شکل توده‌ای ... شرکت کردند», and «برای هفته‌ها» (for weeks) -> «چندین هفته»."
    },
    {
        "ID": "SM-899-03",
        "Project": "Encyclopedia of Social & Political Movements (Vol. 1)",
        "Chapter_Entry": "Entry 899: Gezi Park Protests (Istanbul)",
        "English_Sentence": "The global diffusion of social unrest driven by deeply rooted political and economic grievances reverberated also in Turkey, where public frustrations with the incumbency of R. Tayyip Erdoğan and the AKP surfaced and became crystallized through resilient, creative forms of demonstration and resistance on the street.",
        "RTS_Version_Invalid": "شیوع جهانی ناآرامی اجتماعی که به واسطۀ نارضایتی‌های سیاسی و اقتصادی عمیق و ریشه‌دار به پیش می‌رفت در ترکیه هم طنین‌انداز شد؛ جایی که ناکامی‌های عمومی از تصدی آر. طیب اردوغان و حزب عدالت و توسعه ظاهر شد و در قالب اشکال خلاقانه و مقاومِ گردهمایی و مقاومت خیابانی متبلور شد.",
        "Human_Edited_Version": "شیوع جهانی ناآرامی اجتماعی که به واسطۀ نارضایتی‌های سیاسی و اقتصادی عمیق و ریشه‌دار به پیش می‌رفت در ترکیه هم طنین‌انداز شد؛ جایی که ناکامی‌های عمومی از تصدی رجب طیب اردوغان و حزب عدالت و توسعه ظاهر شد و در قالب اشکال خلاقانه و بادوامی از گردهمایی و مقاومت خیابانی متبلور شد.",
        "Error_Category": "Lexical Anti-Repetition & Name Standard",
        "Editorial_Rationale": "Eliminate root repetition «مقاوم ... مقاومت» in the same clause by rendering resilient as «بادوام»; expand English initial «R. Tayyip Erdoğan» to full standard Persian «رجب طیب اردوغان»."
    },
    {
        "ID": "SM-899-04",
        "Project": "Encyclopedia of Social & Political Movements (Vol. 1)",
        "Chapter_Entry": "Entry 899: Gezi Park Protests (Istanbul)",
        "English_Sentence": "Having been in power for more than ten years by the time of the protests, Erdoğan had succeeded in securing landslide victories in consecutive elections, which led to single-party governments with parliamentary majorities. At the same time, he personified a progressively authoritarian politics by capitalizing on the control of media, repression, and exclusion.",
        "RTS_Version_Invalid": "اردوغان که تا زمان اعتراضات بیش از ده سال در قدرت بود، با جلب اکثریت قاطع در انتخابات متوالی موفق به پیروزی‌هایی شده بود که منجر به دولت‌های تک‌حزبی با اکثریت پارلمانی شد. هم‌زمان، او از طریق بهره بردن از کنترل رسانه‌ای، سرکوب و طرد، به سیاست اقتدارگرایانۀ فزاینده‌ای تجسم بخشید.",
        "Human_Edited_Version": "اردوغان که تا زمان اعتراضات بیش از ده سال در قدرت بود، با جلب اکثریت قاطع در انتخابات متوالی موفق به پیروزی‌هایی شده بود که منجر به تشکیل کابینه‌های تک‌حزبی با اکثریت پارلمانی شد. هم‌زمان، او با اتکا به کنترل رسانه‌ای، سرکوب و طرد، به سیاست اقتدارگرایانۀ فزاینده‌ای تجسم بخشید.",
        "Error_Category": "Terminology & Register Precision",
        "Editorial_Rationale": "Render «single-party governments» in a parliamentary context precisely as «تشکیل کابینه‌های تک‌حزبی» rather than ambiguous «دولت‌های تک‌حزبی»; tighten «از طریق بهره بردن از» to «با اتکا به»."
    },
    {
        "ID": "SM-899-05",
        "Project": "Encyclopedia of Social & Political Movements (Vol. 1)",
        "Chapter_Entry": "Entry 899: Gezi Park Protests (Istanbul)",
        "English_Sentence": "The demolition of Gezi Park thus represented the embodiment of a political machinery that, under the banner of popular will, has been punishing recalcitrant students, Kurds, women, labor unionists, Alevis, and others by teargas and incarceration, while allowing construction giants to aggressively commodify the urban environment (Lovering and Türkmen 2011).",
        "RTS_Version_Invalid": "بنابراین تخریب پارک گزی دستگاه سیاسی‌ای را متجسم می‌کرد که ذیل پرچم خواست همگانی، دانشجویان نافرمان، کردها، زنان، سندیکالیست‌های کارگری، علوی‌ها و دیگران را با گاز اشک‌آور و حبس مجازات می‌کرد، در حالی که به غول‌های ساخت‌وساز اجازه می‌داد به شکلی تهاجمی محیط شهری را کالایی کنند (Lovering and Türkmen 2011).",
        "Human_Edited_Version": "به این اعتبار، تخریب پارک گزی تجسم همان دستگاه سیاسی بود که ذیل پرچم خواست همگانی، دانشجویان متمرد، کردها، زنان، سندیکالیست‌های کارگری، علوی‌ها و دیگران را با گاز اشک‌آور و حبس مجازات می‌کرد، در حالی که به غول‌های ساخت‌وساز اجازه می‌داد به شکلی تهاجمی محیط شهری را کالایی کنند (Lovering and Türkmen 2011).",
        "Error_Category": "Calque Eradication & Lexical Elevation",
        "Editorial_Rationale": "Replace awkward transitive calque «دستگاه سیاسی‌ای را متجسم می‌کرد» with natural Persian «تجسم همان دستگاه سیاسی بود»; elevate «دانشجویان نافرمان» (recalcitrant students) to «دانشجویان متمرد»."
    },
    {
        "ID": "SM-899-06",
        "Project": "Encyclopedia of Social & Political Movements (Vol. 1)",
        "Chapter_Entry": "Entry 899: Gezi Park Protests (Istanbul)",
        "English_Sentence": "This picture is nonetheless nuanced by analyses that refute middle-class theses and the predominance of young professionals as the main social engine behind Gezi Park mobilizations. According to this latter view, the social fabric of the protests can be better understood in terms of a shared political and cultural opposition to Erdoğan and the AKP, rather than by mere reference to class (Yörük and Yüksel 2014).",
        "RTS_Version_Invalid": "با این وجود، این تصویر با تحلیل‌هایی که نظریه‌های طبقۀ متوسط و غلبۀ متخصصان جوان را به‌عنوان موتور اجتماعی اصلی بسیج‌های پارک گزی رد می‌کنند، دقیق‌تر و ظریف‌تر می‌شود. براساس دیدگاه اخیر، بافت اجتماعی اعتراضات را برحسب مخالفت سیاسی و فرهنگیِ مشترک با اردوغان و حزب عدالت و توسعه، بهتر از ارجاعِ صرف به طبقه می‌توان فهمید (Yoruk and Yuksel 2014).",
        "Human_Edited_Version": "اما با اضافه کردن تحلیل‌های دیگری که نظریه‌های طبقۀ متوسط و غلبۀ متخصصان جوان را به‌عنوان موتور اجتماعی اصلی بسیج‌های پارک گزی رد می‌کنند، تصویر دقیق‌تر و ظریف‌تری از این اعتراضات به دست می‌آید. براساس دیدگاه دوم، بافت اجتماعی اعتراضات را برحسب مخالفت سیاسی و فرهنگیِ مشترک با اردوغان و حزب عدالت و توسعه، بهتر از ارجاعِ صرف به طبقه می‌توان فهمید (Yoruk and Yuksel 2014).",
        "Error_Category": "De-Passivization & Discourse Reference",
        "Editorial_Rationale": "Convert English passive «This picture is nonetheless nuanced by analyses that...» into active adverbial clause «اما با اضافه کردن تحلیل‌های دیگری که...، تصویر دقیق‌تر و ظریف‌تری ... به دست می‌آید»; fix calque «دیدگاه اخیر» (this latter view) to «دیدگاه دوم»."
    },
    {
        "ID": "SM-899-07",
        "Project": "Encyclopedia of Social & Political Movements (Vol. 1)",
        "Chapter_Entry": "Entry 899: Gezi Park Protests (Istanbul)",
        "English_Sentence": "However, broader demands articulated by Taksim Solidarity concerning restrictions on the exercise of freedom of assembly and expression on the one hand, and police brutality and arbitrary use of less-than-lethal weapons on the other, have largely remained unmet.",
        "RTS_Version_Invalid": "با این حال، خواسته‌های گسترده‌تر مطرح‌شده توسط جنبش همبستگی تکسیم در مورد محدودیت‌های اعمال آزادی تجمع و بیان از یک سو، و خشونت پلیس و استفادۀ خودسرانه از سلاح‌های غیرکشنده از سوی دیگر، تا حد زیادی برآورده نشده است.",
        "Human_Edited_Version": "با این حال، خواسته‌های گسترده‌تر مطرح‌شده توسط جنبش همبستگی تکسیم عمدتاً برآورده نشده است، یعنی از یک سو مطالبه برای رفع محدودیت‌های آزادی تجمع و بیان، و از سوی دیگر پایان دادن به خشونت پلیسی و استفادۀ خودسرانه از سلاح‌های غیرکشنده.",
        "Error_Category": "Syntactic Extraposition & Semantic Unpacking",
        "Editorial_Rationale": "Place the verb «عمدتاً برآورده نشده است» before the long two-part modifier («یعنی از یک سو... و از سوی دیگر...»); unpack compressed English «demands concerning restrictions... and police brutality» by adding «رفع» and «پایان دادن به» to avoid semantic ambiguity."
    },
    {
        "ID": "SM-899-08",
        "Project": "Encyclopedia of Social & Political Movements (Vol. 1)",
        "Chapter_Entry": "Entry 899: Gezi Park Protests (Istanbul)",
        "English_Sentence": "The long-term consequences of Gezi, on the other hand, will be judged by history.",
        "RTS_Version_Invalid": "از سوی دیگر، عواقب بلندمدت گزی از سوی تاریخ قضاوت خواهد شد.",
        "Human_Edited_Version": "از این روی، عواقب بلندمدت گزی توسط تاریخ قضاوت خواهد شد.",
        "Error_Category": "Phonetic Anti-Repetition",
        "Editorial_Rationale": "Eliminate adjacent repetition of «از سوی دیگر ... از سوی تاریخ» in a short sentence."
    },
    {
        "ID": "SM-901-01",
        "Project": "Encyclopedia of Social & Political Movements (Vol. 1)",
        "Chapter_Entry": "Entry 901: Global Austerity Protests",
        "English_Sentence": "Scholars group such measures into a family of like-minded policies that include a wide range of governmental actions, including: subsidy cuts to lower- and middle-class groups, wage freezes, price increases, massive layoffs, regressive taxation, deregulation, privatization, and free trade (Walton and Seddon 1994; Almeida and Chase-Dunn 2018).",
        "RTS_Version_Invalid": "صاحب‌نظران این برنامه‌ها را در خانواده‌ای از سیاست‌های هم‌سو دسته‌بندی می‌کنند که شامل دامنۀ گسترده‌ای از اقدامات دولتی است، از جمله: قطع یارانه‌ها برای گروه‌های طبقات پایین و متوسط، تثبیت دستمزدها، افزایش قیمت‌ها، اخراج‌های گسترده، مالیات‌بندی تنازلی، مقررات‌زدایی، خصوصی‌سازی و تجارت آزاد (Walton and Seddon 1994; Almeida and Chase-Dunn 2018).",
        "Human_Edited_Version": "صاحب‌نظران این برنامه‌ها را در خانواده‌ای از سیاست‌های هم‌سو دسته‌بندی می‌کنند که شامل دامنۀ گسترده‌ای از اقدامات دولتی است، از جمله: قطع یارانه‌ها برای گروه‌های اجتماعی متعلق به طبقات پایین و متوسط، انجماد دستمزدها، افزایش قیمت‌ها، اخراج‌های گسترده، مالیات‌بندی تنازلی، مقررات‌زدایی، خصوصی‌سازی و تجارت آزاد (Walton and Seddon 1994; Almeida and Chase-Dunn 2018).",
        "Error_Category": "Terminology & Contextual Precision",
        "Editorial_Rationale": "In austerity contexts, «wage freezes» means halting wage increases despite inflation («انجماد دستمزدها»), whereas «تثبیت دستمزدها» has a positive connotation. Also clarify «گروه‌های طبقات پایین و متوسط» as «گروه‌های اجتماعی متعلق به طبقات پایین و متوسط»."
    },
    {
        "ID": "SM-901-02",
        "Project": "Encyclopedia of Social & Political Movements (Vol. 1)",
        "Chapter_Entry": "Entry 901: Global Austerity Protests",
        "English_Sentence": "Because economic-based protests are some of the largest and most common forms of contention, their causal determinants and political consequences offer important insights into the dynamics of collective action in general.",
        "RTS_Version_Invalid": "ازآنجاکه اعتراضات اقتصادبنیان برخی از بزرگ‌ترین و عام‌ترین اشکال ستیز هستند، عوامل تعیین‌کنندۀ علّی و پیامدهای سیاسی آن‌ها بصیرت‌های مهمی دربارۀ پویایی‌های کنش جمعی به‌طور عام به دست می‌دهند.",
        "Human_Edited_Version": "اعتراضات اقتصادی از جمله بزرگ‌ترین و رایج‌ترین اشکال ستیز هستند. از این رو، علّت‌های تعیین‌کنندۀ آن‌ها، و نیز پیامدهای سیاسی‌شان بینش‌ها و نکاتی راهگشا دربارۀ پویایی‌های کنش جمعی به‌طور عام به دست می‌دهند.",
        "Error_Category": "Causal Sentence Splitting & Anti-Repetition",
        "Editorial_Rationale": "Split heavy «Because X, Y» sentence into two sentences connected by «از این رو،»; replace artificial coinage «اعتراضات اقتصادبنیان» with «اعتراضات اقتصادی»; replace pleonastic «عوامل تعیین‌کنندۀ علّی» with «علّت‌های تعیین‌کننده»; avoid repeating «عام‌ترین ... به‌طور عام» by using «رایج‌ترین»; render «important insights» as «بینش‌ها و نکاتی راهگشا»."
    },
    {
        "ID": "SM-901-03",
        "Project": "Encyclopedia of Social & Political Movements (Vol. 1)",
        "Chapter_Entry": "Entry 901: Global Austerity Protests",
        "English_Sentence": "With the global economic slowdown in the early 1970s, many governments in the global North faced a fiscal crisis of the state whereby they had difficulties maintaining public budgets following 20–25 years of unprecedented economic growth.",
        "RTS_Version_Invalid": "با کند شدن رشد اقتصاد جهانی در اوایل دهۀ 1970، بسیاری از دولت‌ها در شمال جهانی با بحران مالی دولت روبه‌رو شدند و به موجب آن، پس از 20 تا 25 سال رشد اقتصادی بی‌نظیر، در حفظ بودجه‌های عمومی با مشکل مواجه شدند.",
        "Human_Edited_Version": "با کند شدن رشد اقتصاد جهانی در اوایل دهۀ 1970، بسیاری از حکومت‌ها در شمال جهانی با بحران مالی دولتی روبه‌رو شدند و به موجب آن، پس از 20 تا 25 سال رشد اقتصادی بی‌نظیر، برای حفظ بودجه‌های عمومی به مشکل برخوردند.",
        "Error_Category": "Lexical & Verbal Anti-Repetition",
        "Editorial_Rationale": "Differentiate «governments» («حکومت‌ها») from «fiscal crisis of the state» («بحران مالی دولتی») to avoid repeating «دولت‌ها ... بحران مالی دولت»; vary consecutive compound verbs («روبه‌رو شدند ... به مشکل برخوردند»)."
    },
    {
        "ID": "SM-901-04",
        "Project": "Encyclopedia of Social & Political Movements (Vol. 1)",
        "Chapter_Entry": "Entry 901: Global Austerity Protests",
        "English_Sentence": "Nonetheless, much of the contention in the 1970s against austerity measures occurred in the global North (with the heavy presence of trade unions in the vanguard of mobilizations) until the onset of the global debt crisis in the early 1980s.",
        "RTS_Version_Invalid": "با این همه، تا پیش از آغاز بحران بدهی جهانی در اوایل دهۀ 1980، بخش عمده‌ای از ستیزها علیه برنامه‌های ریاضتی در دهۀ 1970 در شمال جهانی (با حضور سنگین اتحادیه‌های کارگری در پیشگامی بسیج‌ها) رخ داد.",
        "Human_Edited_Version": "با این همه، بخش عمده‌ای از ستیزها علیه برنامه‌های ریاضتی در دهۀ 1970 در شمال جهانی و با حضور سنگین اتحادیه‌های کارگری در مقام پیشگام بسیج‌ها صورت گرفت، و تا اوایل دهۀ 1980 یعنی تا آغاز بحران بدهی جهانی ادامه یافت.",
        "Error_Category": "Chronological Logic & Monolingual Sense-Check",
        "Editorial_Rationale": "Fronting the «until...» clause created a chronological tautology in Persian («Before the early 1980s, the contention of the 1970s occurred...»). Keep chronological sequence and unpack the temporal extension at the end («...صورت گرفت، و تا اوایل دهۀ 1980 یعنی تا آغاز بحران بدهی جهانی ادامه یافت»)."
    },
    {
        "ID": "SM-901-05",
        "Project": "Encyclopedia of Social & Political Movements (Vol. 1)",
        "Chapter_Entry": "Entry 901: Global Austerity Protests",
        "English_Sentence": "Almeida (2010, 307) summarizes the debt crisis and the intervention of international financial institutions as follows:",
        "RTS_Version_Invalid": "آلمیدا (Almeida 2010, 307) بحران بدهی و مداخلۀ نهادهای مالی بین‌المللی را این‌طور تلخیص می‌کند:",
        "Human_Edited_Version": "آلمیدا (Almeida 2010, 307) بحران بدهی و مداخلۀ نهادهای مالی بین‌المللی را این‌طور خلاصه می‌کند:",
        "Error_Category": "Register & Idiomatic Simplicity",
        "Editorial_Rationale": "Prefer transparent, natural Persian «خلاصه می‌کند» over stiff bureaucratic/archaic «تلخیص می‌کند»."
    },
    {
        "ID": "SM-901-06",
        "Project": "Encyclopedia of Social & Political Movements (Vol. 1)",
        "Chapter_Entry": "Entry 901: Global Austerity Protests",
        "English_Sentence": "Between 1981 and 2008, most countries in the global South had been under some kind of structural adjustment program for more than 10 years (Abouharb and Duchesne 2019; Chase-Dunn and Almeida 2020; Almeida and Pérez Martín 2021). This moved the epicenter of resistance to austerity from Europe to the global South until the global recession of 2008/2009.",
        "RTS_Version_Invalid": "بین سال‌های 1981 و 2008 بیشتر کشورهای جنوب جهانی بیش از 10 سال تحت نوعی برنامۀ تعدیل ساختاری قرار داشتند (Abouharb and Duchesne 2019; Chase-Dunn and Almeida 2020; Almeida and Pérez Martín 2021). این امر تا زمان رکود جهانی 2008/2009 کانون مقاومت در برابر ریاضت اقتصادی را از اروپا به جنوب جهانی منتقل کرد.",
        "Human_Edited_Version": "بین سال‌های 1981 و 2008 اکثر کشورهای جنوب جهانی بیش از ده سال را تحت شکلی از برنامۀ تعدیل ساختاری سپری کرده بودند (Abouharb and Duchesne 2019; Chase-Dunn and Almeida 2020; Almeida and Pérez Martín 2021). به این ترتیب، کانون مقاومت در برابر ریاضت اقتصادی تا زمان رکود جهانی 2008/2009 از اروپا به جنوب جهانی منتقل شده بود.",
        "Error_Category": "Phonetic Anti-Repetition & Inanimate Subject Eradication",
        "Editorial_Rationale": "Avoid phonetic collision «بیشتر ... بیش از» by using «اکثر ... بیش از ده سال»; replace static «قرار داشتند» with «سپری کرده بودند»; replace inanimate calque «این امر ... منتقل کرد» (This moved...) with «به این ترتیب، ... منتقل شده بود»."
    },
    {
        "ID": "SM-901-07",
        "Project": "Encyclopedia of Social & Political Movements (Vol. 1)",
        "Chapter_Entry": "Entry 901: Global Austerity Protests",
        "English_Sentence": "In the latter cases, left-oriented oppositional political parties effectively capture the energy and claims of the anti-neoliberal protest wave and transform disruptive demonstrations, roadblocks, and labor strikes into institutionalized challenges for social change.",
        "RTS_Version_Invalid": "در این موارد دوم، احزاب سیاسی مخالف و چپ‌گرا به‌طور مؤثری انرژی و مطالبات موج اعتراضی ضدنئولیبرالی را جذب می‌کنند و تظاهرات اخلال‌گرانه، راه‌بندان‌ها و اعتصابات کارگری را به چالش‌های نهادینه‌شده برای تغییر اجتماعی تبدیل می‌کنند.",
        "Human_Edited_Version": "در حالت دوم، احزاب سیاسی مخالف و چپ‌گرا به‌طور مؤثری انرژی و مطالبات موج اعتراضی ضدنئولیبرالی را جذب می‌کنند و تظاهرات اخلال‌گرانه، راه‌بندان‌ها و اعتصابات کارگری را به چالش‌های نهادینه‌شده برای تغییر اجتماعی تبدیل می‌کنند.",
        "Error_Category": "Idiomatic Discourse Connector",
        "Editorial_Rationale": "Render «In the latter cases» (contrasting two macro-level outcomes) naturally as «در حالت دوم» rather than the literal calque «در این موارد دوم»."
    },
    {
        "ID": "SM-901-08",
        "Project": "Encyclopedia of Social & Political Movements (Vol. 1)",
        "Chapter_Entry": "Entry 901: Global Austerity Protests",
        "English_Sentence": "In Africa, in 1985, only 14 countries had a privatization policy on the public agenda, but, by 1990, 40 African nations (90% of countries on the continent) were preparing a major program of privatization (Young 1991, 51).",
        "RTS_Version_Invalid": "در افریقا، در سال 1985، فقط 14 کشور سیاست خصوصی‌سازی را در دستور کار عمومی داشتند، لیکن تا سال 1990، 40 کشور افریقایی (90 درصد کشورهای قاره) در حال آماده‌سازی برنامۀ کلانی برای خصوصی‌سازی بودند (Young 1991, 51).",
        "Human_Edited_Version": "در آفریقا، در سال 1985، فقط 14 کشور سیاست خصوصی‌سازی را در دستور کار عمومی داشتند، لیکن تا سال 1990، 40 کشور آفریقایی (90 درصد کشورهای قاره) در حال آماده‌سازی برنامۀ کلانی برای خصوصی‌سازی بودند (Young 1991, 51).",
        "Error_Category": "Orthographic Standardization",
        "Editorial_Rationale": "Standardize spelling of «آفریقا / آفریقایی» with initial «آ» across all entries."
    }
]

UNIVERSAL_GLOSSARY = [
    {
        "Term_ID": "GL-001",
        "English_Term": "Contentious Politics",
        "Preferred_Persian": "سیاست ستیز / سیاست منازعه‌گرایانه",
        "Alternative_or_Rejected": "سیاست‌های ستیزه‌جویانه / سیاست جدلی (آشوری: ستیهش / جدل)",
        "Used_By_Attribution": "Dr. Saeed Madani & RTS Studio (Encyclopedia of Social Movements); Ali المرشدی / Iranian Sociology Translations of Tilly & Tarrow; cf. Dariush Ashouri (فرهنگ علوم انسانی: ستیهنده / جدل‌انگیز)",
        "Theoretical_Lineage": "Charles Tilly, Sidney Tarrow, Doug McAdam",
        "Domain": "Social Movements / Political Sociology",
        "Usage_Notes": "Refers to collective political struggle and disruptive claim-making against authorities; avoid «ستیزه‌جویانه» which implies psychological belligerence."
    },
    {
        "Term_ID": "GL-002",
        "English_Term": "Repertoire of Contention",
        "Preferred_Persian": "خزانۀ ستیز / گنجینۀ ستیز (رپرتوار ستیز)",
        "Alternative_or_Rejected": "فهرست منازعه / جعبه ابزار اعتراض (آشوری برای repertoire: انبانۀ برنامه / کار-انبان)",
        "Used_By_Attribution": "Dr. Saeed Madani & RTS Studio (Entries 899, 1009); Persian translations of Charles Tilly; cf. Dariush Ashouri (فرهنگ علوم انسانی: انبانه / رپرتوار)",
        "Theoretical_Lineage": "Charles Tilly",
        "Domain": "Social Movements",
        "Usage_Notes": "Historically learned and culturally shared set of protest routines (strikes, petitions, barricades, hunger strikes) available to collective actors."
    },
    {
        "Term_ID": "GL-003",
        "English_Term": "Resource Mobilization Theory",
        "Preferred_Persian": "نظریۀ بسیج منابع",
        "Alternative_or_Rejected": "نظریۀ تجهیز منابع",
        "Used_By_Attribution": "Standard Iranian Sociological Consensus; Dr. Saeed Madani & RTS Studio (Encyclopedia of Social Movements)",
        "Theoretical_Lineage": "John D. McCarthy & Mayer N. Zald",
        "Domain": "Social Movements",
        "Usage_Notes": "Emphasizes organizational infrastructure, material/symbolic resources, and rationality over crowd psychology."
    },
    {
        "Term_ID": "GL-004",
        "English_Term": "Political Opportunity Structure",
        "Preferred_Persian": "ساختار فرصت‌های سیاسی / ساختار فرصت سیاسی",
        "Alternative_or_Rejected": "ساختار موقعیت سیاسی",
        "Used_By_Attribution": "Dr. Saeed Madani & RTS Studio (Entry 871); Established Persian Sociology Literature",
        "Theoretical_Lineage": "Peter Eisinger, Sidney Tarrow, Doug McAdam, Charles Tilly",
        "Domain": "Social Movements / Political Science",
        "Usage_Notes": "Openings, elite divisions, and institutional alignments in the formal political system that encourage or constrain mobilization."
    },
    {
        "Term_ID": "GL-005",
        "English_Term": "Political Process Model",
        "Preferred_Persian": "الگوی فرایند سیاسی",
        "Alternative_or_Rejected": "مدل پروسۀ سیاسی",
        "Used_By_Attribution": "RTS Studio & Encyclopedia of Social Movements",
        "Theoretical_Lineage": "Doug McAdam",
        "Domain": "Social Movements",
        "Usage_Notes": "Links political opportunities, indigenous organizational strength, and cognitive liberation."
    },
    {
        "Term_ID": "GL-006",
        "English_Term": "Framing Processes / Frame Alignment",
        "Preferred_Persian": "فرایندهای چارچوب‌بندی / هم‌راستایی چارچوب‌ها",
        "Alternative_or_Rejected": "قالب‌بندی / کادربندی (آشوری در فرهنگ علوم انسانی: قالب‌بندی / کادربندی)",
        "Used_By_Attribution": "RTS Studio & Encyclopedia of Social Movements (preferred in sociology); cf. Dariush Ashouri (فرهنگ علوم انسانی: قالب‌بندی / کادربندی)",
        "Theoretical_Lineage": "Erving Goffman, David A. Snow, Robert D. Benford",
        "Domain": "Social Movements / Cultural Sociology",
        "Usage_Notes": "In contemporary Iranian sociology, «چارچوب‌بندی» is universally established over «قالب‌بندی» for Goffman and Snow's framing theory."
    },
    {
        "Term_ID": "GL-007",
        "English_Term": "Social Movement Sector (SMS)",
        "Preferred_Persian": "بخش جنبش اجتماعی / بخش جنبش‌های اجتماعی",
        "Alternative_or_Rejected": "سکتور جنبش اجتماعی",
        "Used_By_Attribution": "Dr. Saeed Madani & RTS Studio (Entry 871)",
        "Theoretical_Lineage": "John D. McCarthy & Mayer N. Zald",
        "Domain": "Social Movements",
        "Usage_Notes": "The configuration of all social movement organizations (SMOs) and industries operating within a society."
    },
    {
        "Term_ID": "GL-008",
        "English_Term": "Collective Identity",
        "Preferred_Persian": "هویت جمعی",
        "Alternative_or_Rejected": "این‌همانی جمعی",
        "Used_By_Attribution": "Standard Iranian Sociology Consensus; RTS Studio",
        "Theoretical_Lineage": "Alberto Melucci",
        "Domain": "Social Movements / Sociology",
        "Usage_Notes": "Shared definition of 'we' produced by interacting individuals in a movement."
    },
    {
        "Term_ID": "GL-009",
        "English_Term": "Free-Rider Problem",
        "Preferred_Persian": "معمای مفت‌سواری / مسئلۀ مفت‌سواری",
        "Alternative_or_Rejected": "مشکل سواری مجانی",
        "Used_By_Attribution": "RTS Studio & Iranian Political Economy / Sociology Consensus",
        "Theoretical_Lineage": "Mancur Olson",
        "Domain": "Rational Choice / Collective Action",
        "Usage_Notes": "Benefiting from collective goods without contributing to the cost of collective action."
    },
    {
        "Term_ID": "GL-010",
        "English_Term": "Global Austerity Protests",
        "Preferred_Persian": "اعتراضات جهانی علیه ریاضت اقتصادی",
        "Alternative_or_Rejected": "اعتراضات ریاضتی جهانی (کژتابی معنایی)",
        "Used_By_Attribution": "Keyvan Mohtadi & RTS Studio Decision (Entry 901)",
        "Theoretical_Lineage": "Paul D. Almeida, John Walton, David Seddon",
        "Domain": "Political Economy / Social Movements",
        "Usage_Notes": "Always include «اقتصادی» and «علیه» («علیه ریاضت اقتصادی» or «ضد ریاضت اقتصادی») to avoid the ambiguous phrase «اعتراضات ریاضتی»."
    },
    {
        "Term_ID": "GL-011",
        "English_Term": "Wage Freezes",
        "Preferred_Persian": "انجماد دستمزدها",
        "Alternative_or_Rejected": "تثبیت دستمزدها (دارای بار مثبت کاذب در فارسی)",
        "Used_By_Attribution": "Keyvan Mohtadi Human Edit (Entry 901)",
        "Theoretical_Lineage": "Paul D. Almeida (Neoliberal Austerity Literature)",
        "Domain": "Political Economy",
        "Usage_Notes": "In austerity packages, wage freezes lock wages despite inflation; «انجماد دستمزدها» accurately captures the punitive halt, whereas «تثبیت» sounds like positive stabilization."
    },
    {
        "Term_ID": "GL-012",
        "English_Term": "Balance-of-Payments Crisis",
        "Preferred_Persian": "بحران تراز پرداخت‌ها",
        "Alternative_or_Rejected": "بحران تعادل دستمزدها (خطای ترجمه)",
        "Used_By_Attribution": "Dariush Ashouri (فرهنگ علوم انسانی، ص ۴۲: تراز پرداخت‌ها) & RTS Studio (Entry 901)",
        "Theoretical_Lineage": "International Political Economy",
        "Domain": "Political Economy",
        "Usage_Notes": "Standard macroeconomic term for severe external account deficit."
    },
    {
        "Term_ID": "GL-013",
        "English_Term": "Debt Rescheduling",
        "Preferred_Persian": "استمهال بدهی / زمان‌بندی مجدد بازپرداخت بدهی",
        "Alternative_or_Rejected": "برنامه‌ریزی مجدد بدهی",
        "Used_By_Attribution": "RTS Studio (Entry 901) & Iranian Economic Literature",
        "Theoretical_Lineage": "IMF / World Bank / Sovereign Debt Literature",
        "Domain": "Political Economy",
        "Usage_Notes": "Deferring or restructuring sovereign debt maturities during financial crises."
    },
    {
        "Term_ID": "GL-014",
        "English_Term": "Structural Adjustment Programs (SAPs)",
        "Preferred_Persian": "برنامه‌های تعدیل ساختاری",
        "Alternative_or_Rejected": "برنامه‌های انطباق ساختاری",
        "Used_By_Attribution": "Standard Iranian Political Economy Consensus; Dr. Saeed Madani & RTS Studio (Entry 901)",
        "Theoretical_Lineage": "IMF / World Bank / Critical Development Studies",
        "Domain": "Political Economy",
        "Usage_Notes": "Conditionality packages mandating fiscal austerity, deregulation, trade liberalization, and privatization."
    },
    {
        "Term_ID": "GL-015",
        "English_Term": "Regressive Taxation",
        "Preferred_Persian": "مالیات‌بندی تنازلی",
        "Alternative_or_Rejected": "مالیات قهقهرایی (خطای ترجمه)",
        "Used_By_Attribution": "RTS Studio (Entry 901) & Public Finance Literature",
        "Theoretical_Lineage": "Public Economics / Fiscal Sociology",
        "Domain": "Political Economy",
        "Usage_Notes": "Taxation that takes a larger percentage of income from low-income earners than from high-income earners (opposite of «مالیات تصاعدی»)."
    },
    {
        "Term_ID": "GL-016",
        "English_Term": "Deregulation",
        "Preferred_Persian": "مقررات‌زدایی",
        "Alternative_or_Rejected": "آزادسازی (تداخل با Liberalization)؛ (آشوری: قیدزدایی)",
        "Used_By_Attribution": "RTS Studio (Entry 901) & Iranian Political Economy Consensus; cf. Dariush Ashouri (فرهنگ علوم انسانی: قیدزدایی)",
        "Theoretical_Lineage": "Neoliberal Policy Studies",
        "Domain": "Political Economy",
        "Usage_Notes": "Keep distinct from «آزادسازی» (Liberalization) and «خصوصی‌سازی» (Privatization)."
    },
    {
        "Term_ID": "GL-017",
        "English_Term": "Fiscal Crisis of the State",
        "Preferred_Persian": "بحران مالی دولتی / بحران مالی دولت",
        "Alternative_or_Rejected": "بحران بودجه‌ای حکومت",
        "Used_By_Attribution": "Keyvan Mohtadi Human Edit (Entry 901: «بحران مالی دولتی» when paired with «حکومت‌ها» in the same sentence)",
        "Theoretical_Lineage": "James O'Connor (1973)",
        "Domain": "Political Economy / Sociology of the State",
        "Usage_Notes": "When the sentence already contains «governments» («حکومت‌ها»), render as «بحران مالی دولتی» to avoid repeating «دولت‌ها ... بحران مالی دولت»."
    },
    {
        "Term_ID": "GL-018",
        "English_Term": "Moral Economy",
        "Preferred_Persian": "اقتصاد اخلاقی",
        "Alternative_or_Rejected": "اخلاق اقتصادی",
        "Used_By_Attribution": "Dr. Saeed Madani & RTS Studio (Entry 901); Persian translations of E.P. Thompson & James C. Scott",
        "Theoretical_Lineage": "E.P. Thompson, James C. Scott",
        "Domain": "Social History / Political Sociology",
        "Usage_Notes": "Popular consensus regarding legitimate subsistence rights and fair prices, whose violation triggers food/austerity riots."
    },
    {
        "Term_ID": "GL-019",
        "English_Term": "Subaltern Groups",
        "Preferred_Persian": "گروه‌های فرودست",
        "Alternative_or_Rejected": "گروه‌های مادون / زیردست (آشوری در فرهنگ علوم انسانی: زیردست / زیرباش)",
        "Used_By_Attribution": "Keyvan Mohtadi (Cognitive Twin Core & RTS Studio, Entry 901); Iranian Critical Theory & Postcolonial Consensus; cf. Dariush Ashouri (فرهنگ علوم انسانی: زیردست)",
        "Theoretical_Lineage": "Antonio Gramsci, Gayatri Spivak, Ranajit Guha",
        "Domain": "Critical Theory / Postcolonial Studies / Political Sociology",
        "Usage_Notes": "«فرودست / گروه‌های فرودست» is the established critical-materialist term in contemporary Persian social theory."
    },
    {
        "Term_ID": "GL-020",
        "English_Term": "Eventful Sociology / Eventful Protest",
        "Preferred_Persian": "جامعه‌شناسی رخدادمحور / اعتراض سرنوشت‌ساز (پرحادثه)",
        "Alternative_or_Rejected": "جامعه‌شناسی پررویداد",
        "Used_By_Attribution": "Dr. Saeed Madani & Keyvan Mohtadi Edit (Entry 899)",
        "Theoretical_Lineage": "William H. Sewell Jr. (1996), Donatella della Porta",
        "Domain": "Historical Sociology / Social Movements",
        "Usage_Notes": "Refers to protests/events that transform structures and generate new subjectivities rather than merely reflecting pre-existing conditions."
    },
    {
        "Term_ID": "GL-021",
        "English_Term": "Politics of Pity",
        "Preferred_Persian": "سیاست ترحم",
        "Alternative_or_Rejected": "سیاست دلسوزی / سیاست شفقت",
        "Used_By_Attribution": "RTS Studio (Entry 1009: Hunger Strikes)",
        "Theoretical_Lineage": "Hannah Arendt, Luc Boltanski (Distant Suffering, 1999)",
        "Domain": "Political Philosophy / Sociology of Humanitarianism",
        "Usage_Notes": "Boltanski's concept analyzing how spectacularized suffering mobilizes third-party public opinion and moral indignation."
    },
    {
        "Term_ID": "GL-022",
        "English_Term": "Prefigurative Politics",
        "Preferred_Persian": "سیاست پیش‌نگرانه / سیاست الگوآفرین (تجسم‌بخش)",
        "Alternative_or_Rejected": "سیاست پیشاشکل‌دهنده",
        "Used_By_Attribution": "RTS Studio (Encyclopedia of Social Movements)",
        "Theoretical_Lineage": "Carl Boggs, Wini Breines, David Graeber, Donatella della Porta",
        "Domain": "Social Movements / Anarchist & New Left Theory",
        "Usage_Notes": "Modes of organization and social relationships within a movement that embody the future society being sought."
    },
    {
        "Term_ID": "GL-023",
        "English_Term": "Transnational Advocacy Network (TAN)",
        "Preferred_Persian": "شبکۀ حمایتگری فراملی",
        "Alternative_or_Rejected": "شبکۀ وکالت فراملی (آشوری برای advocacy: هواداری / پشتیبانی)",
        "Used_By_Attribution": "RTS Studio & Iranian International Relations / NGO Literature; cf. Dariush Ashouri (فرهنگ علوم انسانی: هواداری / پشتیبانی)",
        "Theoretical_Lineage": "Margaret E. Keck & Kathryn Sikkink (1998)",
        "Domain": "Transnational Social Movements / International Relations",
        "Usage_Notes": "Networks of activists and NGOs operating across borders to pressure states via the 'boomerang effect'."
    },
    {
        "Term_ID": "GL-024",
        "English_Term": "World Social Forum (WSF) / World Economic Forum (WEF)",
        "Preferred_Persian": "مجمع جهانی اجتماعی / مجمع جهانی اقتصاد",
        "Alternative_or_Rejected": "فروم اجتماعی جهان / مجمع اقتصادی جهانی",
        "Used_By_Attribution": "Dr. Saeed Madani & RTS Studio (Entry 901)",
        "Theoretical_Lineage": "Global Justice Movement / Alter-Globalization",
        "Domain": "Global Studies / Social Movements",
        "Usage_Notes": "Official established Persian titles for WSF (Porto Alegre) and WEF (Davos)."
    },
    {
        "Term_ID": "GL-025",
        "English_Term": "Economically Based Protests",
        "Preferred_Persian": "اعتراضات اقتصادی",
        "Alternative_or_Rejected": "اعتراضات اقتصادبنیان (واژه‌سازی تصنعی)",
        "Used_By_Attribution": "Keyvan Mohtadi Human Edit (Entry 901)",
        "Theoretical_Lineage": "Paul D. Almeida",
        "Domain": "Social Movements / Political Economy",
        "Usage_Notes": "Prefer natural, transparent Persian «اعتراضات اقتصادی» over synthetic compound adjectives like «اقتصادبنیان»."
    },
    {
        "Term_ID": "GL-026",
        "English_Term": "Causal Determinants",
        "Preferred_Persian": "علّت‌های تعیین‌کننده",
        "Alternative_or_Rejected": "عوامل تعیین‌کنندۀ علّی (حشو) / تعیین‌کننده‌های علّی",
        "Used_By_Attribution": "Keyvan Mohtadi Human Edit (Entry 901)",
        "Theoretical_Lineage": "Methodology of Social Sciences",
        "Domain": "Sociology / Methodology",
        "Usage_Notes": "Avoid the pleonastic translationese «عوامل تعیین‌کنندۀ علّی»; «علّت‌های تعیین‌کننده» is direct, natural, and exact."
    }
]


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]):
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        writer.writerows(rows)


def build_sentence_decisions_md(rows: list[dict]) -> str:
    lines = [
        "# RTS Master Sentence Decision Log (Human Preference Corpus)",
        "",
        "This document records sentence-level editorial interventions where the initial **RTS Version** was revised by **Human Editorial Decision (Keyvan Mohtadi)**.",
        "It serves as a cross-project contrastive learning resource showing *what was invalid or suboptimal in the RTS output* and *how human editorial judgment resolved it*.",
        "",
        "- **Machine/Spreadsheet File:** [`sentence_decisions.csv`](./sentence_decisions.csv)",
        "- **Total Logged Decisions:** " + str(len(rows)),
        "",
        "| ID | Project & Entry | English Sentence | RTS Version (Invalid / Rejected) | Human Edited Version (Approved) | Error Category | Editorial Rationale |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
    ]
    for r in rows:
        proj_entry = f"**{r['Project']}**<br>_{r['Chapter_Entry']}_"
        lines.append(
            f"| `{r['ID']}` | {proj_entry} | {r['English_Sentence']} | <div dir=\"rtl\">{r['RTS_Version_Invalid']}</div> | <div dir=\"rtl\">{r['Human_Edited_Version']}</div> | `{r['Error_Category']}` | {r['Editorial_Rationale']} |"
        )
    lines.append("")
    return "\n".join(lines)


def build_universal_glossary_md(rows: list[dict]) -> str:
    lines = [
        "# RTS Universal Glossary & Conceptual Genealogy",
        "",
        "Cross-project master glossary of preferred Persian equivalents across sociology, political economy, philosophy, and critical theory.",
        "Includes explicit attribution of **who coined or used each term**—drawing from both authoritative Persian reference works (e.g., Dariush Ashouri, established translations) and our own translation/editorial decisions.",
        "",
        "- **Machine/Spreadsheet File:** [`universal_glossary.csv`](./universal_glossary.csv)",
        "- **Total Logged Terms:** " + str(len(rows)),
        "",
        "| ID | English Term | Preferred Persian Translation | Alternative / Rejected Forms | Used By (Reference / Translator Attribution) | Theoretical Lineage | Domain | Usage Notes |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
    ]
    for r in rows:
        lines.append(
            f"| `{r['Term_ID']}` | **{r['English_Term']}** | <div dir=\"rtl\">**{r['Preferred_Persian']}**</div> | <div dir=\"rtl\">{r['Alternative_or_Rejected']}</div> | {r['Used_By_Attribution']} | {r['Theoretical_Lineage']} | `{r['Domain']}` | {r['Usage_Notes']} |"
        )
    lines.append("")
    return "\n".join(lines)


def build_readme(num_decisions: int, num_terms: int) -> str:
    return f"""# RTS Master Corpus & Universal Glossary
### Rhizomatique Translation Studio (RTS) — Directed by Keyvan Mohtadi

This repository is the cross-project **Living Editorial Memory** and **Universal Glossary** of the Rhizomatique Translation Studio (RTS). It is updated continuously at the conclusion of each chapter or entry across our translation and editing projects.

Rather than hardcoding static rules into every prompt, this repository accumulates empirical editorial decisions over time so that both human collaborators and our AI pipeline can study, audit, and learn from our evolving translation praxis.

---

## 📂 Repository Contents

### 1. Contrastive Sentence Decision Log (`English` $\\to$ `RTS Invalid` $\\to$ `Human Edited`)
Tracks specific sentences where the RTS draft was judged invalid, mechanical, calqued, or rhythmically flawed, alongside Keyvan Mohtadi's final human edit and the distilled rationale.
- 📊 **CSV (Excel / Google Sheets / Data Pipeline):** [`sentence_decisions.csv`](./sentence_decisions.csv)
- 📖 **Browsable Markdown Table:** [`SENTENCE_DECISIONS.md`](./SENTENCE_DECISIONS.md) *(Currently logging **{num_decisions}** verified sentence-level decisions)*

### 2. Universal Glossary & Attribution Database
Records our preferred Persian translations for core concepts across sociology, political economy, philosophy, and cultural studies—explicitly documenting **who used or coined the term** (whether from reference dictionaries like Dariush Ashouri's *Dictionary of Humanities*, established Persian translators, project translators like Dr. Saeed Madani, or RTS editorial decisions).
- 📊 **CSV (Excel / Google Sheets / Data Pipeline):** [`universal_glossary.csv`](./universal_glossary.csv)
- 📖 **Browsable Markdown Table:** [`UNIVERSAL_GLOSSARY.md`](./UNIVERSAL_GLOSSARY.md) *(Currently logging **{num_terms}** core conceptual terms)*

---

## 🔄 How We Update This Repository (End-of-Chapter Workflow)

1. **Human Editorial Pass:** At the end of each chapter/entry, the human editor finalizes the Persian text.
2. **Automated Diff Extraction:** We compare the **RTS Draft** against the **Human Final Version**, extracting sentences with substantive syntactic, lexical, chronological, or stylistic revisions.
3. **Corpus & Glossary Update:** New sentence pairs and newly settled terminology (with their reference/translator attributions) are appended to `sentence_decisions.csv` and `universal_glossary.csv`.
4. **Markdown Sync:** Running `python scripts/build_corpus.py` regenerates the GitHub Markdown tables (`SENTENCE_DECISIONS.md` and `UNIVERSAL_GLOSSARY.md`) so collaborators can browse everything directly on GitHub or download the CSVs.
"""


def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    sent_fields = [
        "ID",
        "Project",
        "Chapter_Entry",
        "English_Sentence",
        "RTS_Version_Invalid",
        "Human_Edited_Version",
        "Error_Category",
        "Editorial_Rationale",
    ]
    gloss_fields = [
        "Term_ID",
        "English_Term",
        "Preferred_Persian",
        "Alternative_or_Rejected",
        "Used_By_Attribution",
        "Theoretical_Lineage",
        "Domain",
        "Usage_Notes",
    ]

    write_csv(ROOT / "sentence_decisions.csv", sent_fields, SENTENCE_DECISIONS)
    write_csv(ROOT / "universal_glossary.csv", gloss_fields, UNIVERSAL_GLOSSARY)

    (ROOT / "SENTENCE_DECISIONS.md").write_text(
        build_sentence_decisions_md(SENTENCE_DECISIONS), encoding="utf-8"
    )
    (ROOT / "UNIVERSAL_GLOSSARY.md").write_text(
        build_universal_glossary_md(UNIVERSAL_GLOSSARY), encoding="utf-8"
    )
    (ROOT / "README.md").write_text(
        build_readme(len(SENTENCE_DECISIONS), len(UNIVERSAL_GLOSSARY)), encoding="utf-8"
    )
    print(f"Successfully generated {len(SENTENCE_DECISIONS)} sentence decisions and {len(UNIVERSAL_GLOSSARY)} glossary terms in {ROOT}")


if __name__ == "__main__":
    main()
