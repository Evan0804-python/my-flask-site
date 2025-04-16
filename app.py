import os
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
# 從環境變數獲取密鑰，如果沒有則使用預設值（僅開發環境）
app.secret_key = os.environ.get('SECRET_KEY', 'dev_key_only_for_development')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/technology')
def technology():
    return render_template('technology.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '')
        company = request.form.get('company', '')
        phone = request.form.get('phone', '')
        email = request.form.get('email', '')
        inquiry_type = request.form.get('inquiry_type', '')
        message = request.form.get('message', '')
        
        # 簡單資料驗證
        if not name or not email or not message:
            flash('請填寫所有必填欄位', 'error')
            return redirect(url_for('contact'))
        
        # 這裡您可以加入實際發送電子郵件的程式碼
        # 或將資料保存到資料庫
        print(f"收到聯絡表單：\n姓名：{name}\n公司：{company}\n電話：{phone}\n" 
              f"電子郵件：{email}\n需求類型：{inquiry_type}\n訊息：{message}")
        
        flash('感謝您的來信，我們會儘快回覆！', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# 生產環境配置
if __name__ == '__main__':
    # 檢查是否在生產環境
    if os.environ.get('FLASK_ENV') == 'production':
        # 生產環境設定
        app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    else:
        # 開發環境設定
        app.run(host='0.0.0.0', port=5000, debug=True)