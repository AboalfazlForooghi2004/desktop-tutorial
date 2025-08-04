
````markdown
# GitLab Issue Creator with Table and Comments

این اسکریپت با استفاده از GitLab API، یک Issue جدید در یک پروژه‌ی GitLab ایجاد می‌کند و یک جدول مشخص به همراه چند نظر (comment) به آن اضافه می‌کند.

---

## 📌 ویژگی‌ها

- ایجاد یک **Issue** جدید در GitLab با جدول HTML/Markdown در توضیحات
- ثبت **سه کامنت** پیش‌فرض زیر Issue
- قابلیت تعیین عنوان Issue از طریق پارامتر خط فرمان

---

## ⚙️ پیش‌نیازها

- Python 3
- کتابخانه‌های زیر (با `pip install` قابل نصب هستند):

```bash
pip install requests
````

* یک GitLab **Personal Access Token** با سطح دسترسی `api` یا `write_repository`

---

## 🛠 تنظیمات اولیه

قبل از اجرای اسکریپت، موارد زیر را در فایل Python تنظیم کنید:

```python
ACCESS_TOKEN = "توکن شما"
PROJECT_ID = "ID پروژه‌ی شما در GitLab"
```

برای پیدا کردن `PROJECT_ID`:

1. وارد پروژه‌ی مورد نظر در GitLab شوید
2. به Settings > General بروید
3. در بخش Project ID شناسه را ببینید

---

## 🚀 نحوه اجرا

```bash
python create_issue.py --title "عنوان مورد نظر برای ایشو"
```

مثال:

```bash
python create_issue.py --title "بررسی تفاوت‌های عملکردی بین ژرف و سیسکو"
```

---

## 🧾 توضیحات فنی

* یک جدول Markdown به صورت پیش‌فرض در توضیحات Issue قرار می‌گیرد.
* سه کامنت بعد از ساخت Issue به آن اضافه می‌شوند.
* آدرس نهایی Issue ساخته‌شده به‌صورت لینک در خروجی چاپ می‌شود.

---

## 🧷 مثال خروجی:

```
Creating issue: بررسی تفاوت‌های عملکردی بین ژرف و سیسکو
Issue created successfully: #23
Issue URL: https://git.zharfpouyan.net/l3-switch/l3-switch/-/issues/23
Comment 1 added successfully.
Comment 2 added successfully.
Comment 3 added successfully.
Done.
```

---

## 🛡 نکات امنیتی

🔐 توکن خود را به اشتراک نگذارید و در فایل‌های عمومی قرار ندهید.

---

## 📄 License

MIT

```

---

اگر خواستی README رو به زبان انگلیسی یا دوزبانه هم تنظیم کنم، فقط کافیه بگی.
```
