# Telegram Study Tracker

A Telegram bot that helps learners record study sessions, review progress, and build consistent study habits.

This is an open-source learning project. Its goal is twofold: deliver a useful application and demonstrate professional Python, Git, documentation, testing, and architecture practices.

The bot's user-facing messages are written in Persian, since it is built for Persian-speaking users. All source code, documentation, and comments remain in English.

## Project status

**Sprint 4 — bot skeleton.** The bot runs and responds to `/start`, `/help`, `/about`, and `/ping`. Study-tracking features have not been implemented yet.

## Planned structure

```text
telegram-study-tracker/
├── docs/                         # Architecture, decisions, and learning notes
├── src/telegram_study_tracker/   # Application package, organized by responsibility
├── tests/                        # Automated tests, mirroring application behavior
├── assets/                       # Non-code project assets, such as diagrams
├── README.md                     # Project overview and contributor entry point
├── ROADMAP.md                    # High-level delivery plan
├── CHANGELOG.md                  # User-visible project changes
├── requirements.txt              # Runtime dependencies
├── .gitignore                    # Files Git must not track
└── LICENSE                       # MIT license
```

`src/` keeps importable application code separate from repository tooling and documentation. The package name uses underscores because Python identifiers cannot use hyphens. `tests/` is separate s[...]

## Getting started

## Run locally

1. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Copy `.env.example` to `.env`, then replace its placeholder with a Telegram bot token. Never commit `.env`.
3. Install the package and its dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   python -m pip install -e .
   ```

4. Run the application:

   ```powershell
   python -m telegram_study_tracker
   ```

The bot currently supports `/start`, `/help`, `/about`, and `/ping`. Study-tracking commands are not implemented yet.

## Development principles

- Deliver one small, testable feature per sprint.
- Prefer simple, explicit code over clever abstractions.
- Record meaningful technical decisions in [`docs/decisions.md`](docs/decisions.md).
- Keep user-facing changes in [`CHANGELOG.md`](CHANGELOG.md).
- Make focused Git commits with clear messages.

## License & Attribution

### English

This project is released under the **[MIT License](LICENSE)**.

#### Legal Terms

The MIT License permits anyone to:
- Use, modify, and distribute this software for any purpose
- Sublicense the software

**Required by law:**
- You must include a copy of the original copyright notice and license text in any copies or substantial portions of the software
- The software is provided "as is," without warranties or liability

For full legal terms, see the [LICENSE](LICENSE) file.

#### Attribution (Requested, Not Required)

While not legally required, attribution to the original project is appreciated whenever practical:

```
Telegram Study Tracker
Created by Abtin Falahati

Repository:
https://github.com/AbtinFalahati/telegram-study-tracker
```

Your attribution helps the open-source community and is deeply appreciated.

---

### فارسی

این پروژه تحت [مجوز MIT](LICENSE) منتشر شده است.

#### شرایط قانونی

مجوز MIT کسی‌ را برای موارد زیر اجازه می‌دهد:
- استفاده، تغییر و توزیع این نرم‌افزار برای هر منظوری
- تحت‌مجوز دادن نرم‌افزار

**لازم‌الاجرا:**
- شما باید اطلاعیه حق نشر اصلی و متن مجوز را در هر کپی یا بخش قابل توجه نرم‌افزار شامل کنید
- نرم‌افزار «همانطور که هست» ارائه می‌شود بدون تضمین یا مسئولیت

برای شرایط کامل، فایل [LICENSE](LICENSE) را ببینید.

#### نسبت‌دهی (درخواست شده، نه الزامی)

اگرچه قانونی الزام‌آور نیست، نسبت‌دهی به پروژه‌ی اصلی هر زمان که عملی باشد قدردانی می‌شود:

```
ردیاب مطالعه تلگرام
ساخته‌شده توسط ابتین فلاحتی

مخزن:
https://github.com/AbtinFalahati/telegram-study-tracker
```

نسبت‌دهی شما به جامعه متن‌باز کمک می‌کند و از ما قدردانی می‌شود.

---

# ردیاب مطالعه تلگرام

یک بات تلگرام که به یادگیرندگان کمک می‌کند جلسات مطالعه‌شان را ثبت کنند، پیشرفت خود را بررسی کنند و عادت‌ه[...]

این یک پروژه‌ی متن‌باز آموزشی است. هدف آن دوگانه است: ساخت یک اپلیکیشن کاربردی و نمایش شیوه‌های حرفه‌ای بر[...]

پیام‌های بات برای کاربران به زبان فارسی نوشته می‌شوند، زیرا این بات برای کاربران فارسی‌زبان ساخته شده است[...]

## وضعیت پروژه

**اسپرینت ۴ — اسکلت بات.** بات اجرا می‌شود و به دستورهای `/start`، `/help`، `/about`، و `/ping` پاسخ می‌دهد. قابلیت‌های ردی�[...]

## شروع به کار

برای راه‌اندازی و اجرای پروژه به‌صورت محلی، بخش «Getting started» در بالای همین سند (به زبان انگلیسی) را دنبال کنی�[...]

## اصول توسعه

- در هر اسپرینت یک قابلیت کوچک و قابل تست ارائه می‌شود.
- کد ساده و صریح به انتزاع‌های پیچیده ترجیح داده می‌شود.
- تصمیم‌های فنی مهم در [`docs/decisions.md`](docs/decisions.md) ثبت می‌شوند.
- تغییرات قابل مشاهده برای کاربر در [`CHANGELOG.md`](CHANGELOG.md) نگه‌داری می‌شوند.
- کامیت‌های Git متمرکز و با پیام‌های شفاف انجام می‌شوند.

## مجوز و نسبت‌دهی

### English

This project is released under the **[MIT License](LICENSE)**.

#### Legal Terms

The MIT License permits anyone to:
- Use, modify, and distribute this software for any purpose
- Sublicense the software

**Required by law:**
- You must include a copy of the original copyright notice and license text in any copies or substantial portions of the software
- The software is provided "as is," without warranties or liability

For full legal terms, see the [LICENSE](LICENSE) file.

#### Attribution (Requested, Not Required)

While not legally required, attribution to the original project is appreciated whenever practical:

```
Telegram Study Tracker
Created by Abtin Falahati

Repository:
https://github.com/AbtinFalahati/telegram-study-tracker
```

Your attribution helps the open-source community and is deeply appreciated.

---

### فارسی

این پروژه تحت [مجوز MIT](LICENSE) منتشر شده است.

#### شرایط قانونی

مجوز MIT کسی‌ را برای موارد زیر اجازه می‌دهد:
- استفاده، تغییر و توزیع این نرم‌افزار برای هر منظوری
- تحت‌مجوز دادن نرم‌افزار

**لازم‌الاجرا:**
- شما باید اطلاعیه حق نشر اصلی و متن مجوز را در هر کپی یا بخش قابل توجه نرم‌افزار شامل کنید
- نرم‌افزار «همانطور که هست» ارائه می‌شود بدون تضمین یا مسئولیت

برای شرایط کامل، فایل [LICENSE](LICENSE) را ببینید.

#### نسبت‌دهی (درخواست شده، نه الزامی)

اگرچه قانونی الزام‌آور نیست، نسبت‌دهی به پروژه‌ی اصلی هر زمان که عملی باشد قدردانی می‌شود:

```
ردیاب مطالعه تلگرام
ساخته‌شده توسط ابتین فلاحتی

مخزن:
https://github.com/AbtinFalahati/telegram-study-tracker
```

نسبت‌دهی شما به جامعه متن‌باز کمک می‌کند و از ما قدردانی می‌شود.
