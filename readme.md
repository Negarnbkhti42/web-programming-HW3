<h1 dir='rtl'>  بخش امتیازی تمرین3: چالش نگار </h1>

<body dir='rtl' >

<section dir='rtl' >
<h2 dir='rtl'>  بخش اول</h2>
<p dir='rtl'>
در این قسمت کار خیلی خاصی وجود نداشت صرفا داکر فایل و default.conf مینویسیم و پس از نوشتن، یک img  برای بخش فرانت اند تولید میکنیم (با توجه به عکس یک)      و بعد با توجه به تصویر میایم یک کانتینر (با توجه به تصویر2) به اسم nginx  ازش میسازیم   و سپس پورتش را به 8000 فوروارد میکنیم تا بالا بیاد که با توجه به تصویر 3 موقعی که میریم توی مرورگر میبینیم که روی پورت8000 به درستی پروژه بالا میاد
</p>

<h3 dir='rtl'>چالش مربوط بدین بخش</h3>
<p dir='rtl'>
توی این بخش داکر فایل میایم یه سری مسیرهایی را بهش میدیم و  و میگیم که توی کانتینر توی تصویری که داره بیاد کجا فایل هارا کپی کنه و موقعی که ما دایرکتوری های تودرتو داریم، مثلا فولدر تو فولدر داریم، این بخش سوال برانگیز بود که چجوری باید کپی کردن ها را هندل کنیم چون شما وقتی یه مسیر بیرونی را میزنید و میگید که فایل های این کپی بشه، میاد تمام دایرکتوری های تودر تو آن را هم میخواند و همگی را در  یک سطر مقصد جدید کپی میکنه و حتی اگه اسکریپت بزنیم که دایرکتوری های داخلی هم بیان و باز براشون فولدر جدیدی ساخته بشه، و در مسیر داخلی کپی بشن، باز بخش های بیرونی را داریم و باعث بالارفتن حجم میشه.
</p>
</section>

</br>
</br>

<section  dir='rtl'>
<h2 dir='rtl'>بخش دوم</h2>
<p dir='rtl'>
در این بخش میخواهیم پایگاه داده مان را بالا بیاریم و با توجه به تصویر یک، اول میایم .....مون را میسازیم به اسم ........ که دیتاهایمان را در آن نگه داری کنیم و با توجه به تصویر یک میایم اول یک کانتینر میسازیم برای اطلاعات دیتایمان و رمز پستگرس را هم میزاریم و به پورت 8008 هم فوروارد میکنیم، حالا مسیر کانتینر را مشخص میکنیم و بهش میگیم که به چه ..... وابسته باشه و روی img پستگرس میاریمش بالا، با توجه به تصویر سوم هم میایم جداولی را که داریم را در کانتینرمان  با دستور ..... ایمپورت میکنیم و برای مثال در اینجا یکی از جداول را آوردیم و حالا با دستور cp docker میایم داده هایی که داریم را میریزیم توی مسیر کانترنرمان و دوباره با ...... میایم دوباره داده هایی که داریم را اطلاعاتی که داریم را میریزیم توی جدول هایمان و با توجه به تصویر چهارم هم خواستیم نشان بدهیم که این داده ها کانسیستنت اند و اگر کانتینرمان را بیاریم پایین و دستور استاپ را بزنیم و بعد دوباره بیاریمش بالا، این داده ها همچنان هستند و حذف نشدند.و توی دستور پنجمم اومدیم یه کانتینر دیگه ساختیم و برای آتنتیکیشن مون جدول و موارد مورد نیازش را گذاشتیم.
</p>
<h3 dir='rtl'>چالش مربوط بدین بخش</h3>

<p dir='rtl'>
میخواهیم بک مان را به این کانتینر متصل کنیم و حالا داده ها را از روی آن بخوانیم و مشکلی که داشتیم این خودش یک چالش بود که میخواستیم زمانی که هاست مان را برای دیتابیس مان مشخص کنیم، پورت مان همان پورتی است که برایش مشخص کردیم و رمزمان را همان انتخاب کرده بودیم اما هاست را نداشتیم که در حالت عادی لوکال هاست است  که برای پیدا کردن هاست یک کانتینر میایم از دستوری که در تصویر ششم لست استفاده میکنیم.
</p>

</section>

</br>
</br>

<section dir='rtl' >
<h2 dir='rtl'>بخش سوم</h2>
<p dir='rtl'>
طبق تصویر 7 میایم متغیرهای انوایرمنت ها را مشخص میکنیم که با دیتابیس مان مطابق باشند و موقعی که توی پست من یک دستوری را میزنیم، مثلا دستور ثبت نام را میزنیم، میبینیم که دستور به درستی ارسال شده و جواب به ما یک توکن میدهد.
در تصویر 8 هم مشاهده میشود که با دستور .... که دیتا بیس را بالا آوردیم، توی یوزر اکانت را اگر نگاه کنیم، درمیابیم که یوزر جدیدی که ساختیم، آنجا ثبت شده ولی خب در این قسمت ما ردیس نداریم و چیزی کش نمیشه و برای این قسمتکاری که باید کرد، طبق تصویر دهم باید کانتینر ردیس بسازیم  و پورت فورواردش میکنیم روی پورت 8020 و طبق تصویر یازدهم هم میایم آدرس جدید را در برنامه میزاریم کخ آدرس رذیس مان بدین صورت است  و بعد برای امتحان کردنش باید طبق تصویر دوازدهم بیایم و مثلا اون یوزر ثبت نام شده را ساین این کنیم و وارد صفحه اش میشود و یک توکن به ما برگردانده میشود و میایم کلاینت ردیس مان را طبق تصویر 13 روی همان پورتی که ساخته بودیم باید کانتینرش را بیاریم بالا و چک میکنیم که ببینیم آییا این کلید  در کش ذخیره شده یا نه، چون ما گفته بودیم که هنگامی که یوزر ساین این میکنه تو برنامه و برایش یک توکن ایجاد میشه، باید بره تو کش بزاره که این توکن ولید است و در تصویر 13 هم میایم توکن را وارد کرده تا از وجود آن مطلع شویم و اگر در کش باشد مقدار ولید برایش ثبت میشه .
</p>
</section>

</br>
</br>

<section  >

<h2 dir='rtl'> بخش چهارم</h2>

<p dir='rtl'>
ما باید توی سرویس ها برای اتصال به localhost بنویسیم docker.host.internal
اما برای من کار نمیکرد
راه حلش این بود که تو ابونتو علاوه بر اون، باید هاست رو هم bind کنیم

موقع اجرای ایمیج:

</p>

<section dir='ltr'>

```
sudo docker run -p 3000:3000 --add-host=host.docker.internal:host-gateway -d shahab/node-web-app

```

</section dir='rtl'>
<p dir='rtl'>
توی داکر کامپوز:
</p>
</section>

<section dir='ltr'>

```

  web:
    build: ./web
    ports:
      - "127.0.0.1:3000:3000"

```

</section>

<section>

<h2 dir='rtl'>
بخش پنجم
</h2>

<div dir='ltr' >

```
compose-auth-1             | 2023/02/17 17:32:16 http: panic serving 172.20.0.1:44462: dial tcp: lookup host.docker.internal: no such host

```

</div>

<div dir='rtl'>
که با این جواب برای سرویس auth این رو اضافه کردم و اوکی شد و توضیحات بیشتر در صفحه زیر قابل مشاهده است.
</div>

<a dir='ltr'>

https:stackoverflowcomquestions70505750lookup-host-docker-internal-no-such-host

</a>

</section>

</body>
