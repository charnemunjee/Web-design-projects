
Movesby_Meg - Flask site with Flask-Mail (demo)
----------------------------------------------

Quick start (local):
1. (Optional) create a virtual environment:
   python -m venv venv
   source venv/bin/activate   # mac/linux
   venv\Scripts\activate    # windows

2. Install requirements:
   pip install -r requirements.txt

3. Configure email (in app.py or via environment variables):
   - MAIL_SERVER, MAIL_PORT, MAIL_USE_TLS, MAIL_USERNAME, MAIL_PASSWORD, MAIL_DEFAULT_SENDER
   - The contact form sends to the placeholder recipient: recipient@example.com

4. Run:
   python app.py

5. Open http://127.0.0.1:5000

Notes:
- Product images are local placeholders in static/images. Replace them with real stock photos by putting your files in static/images and keeping the filenames:
    vo2_tank.jpg, vo2_leggings.jpg, vo2_hoodie.jpg, hero.jpg, recipe1.jpg, recipe2.jpg, recipe3.jpg
- The neon AI Chapter logo is in static/images/ai_chapter_neon.png. If you want an SVG or color tweak, tell me and I can regenerate it.
