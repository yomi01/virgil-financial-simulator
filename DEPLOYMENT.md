# 🚀 Deployment Guide - Virgil Financial Simulator

This guide provides step-by-step instructions for deploying the Virgil Financial Simulator on various platforms.

## 📋 Quick Start

### Local Development (Recommended for Testing)

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd virgil-financial-simulator
   ```

2. **Easy setup using provided scripts**
   - **Windows**: Double-click `run.bat` or run from command prompt
   - **Linux/Mac**: Run `./run.sh` in terminal

3. **Manual setup** (if scripts don't work)
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   streamlit run app.py
   ```

4. **Access the app** at `http://localhost:8501`

## 🌐 Cloud Deployment Options

### 1. Streamlit Cloud (Free & Easiest)

**Prerequisites**: GitHub account

**Steps**:
1. Push your code to a GitHub repository
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select your repository
5. Set main file path to `app.py`
6. Click "Deploy"

**Advantages**:
- ✅ Free hosting
- ✅ Automatic deployments from GitHub
- ✅ Built-in SSL certificates
- ✅ Easy domain management

### 2. Heroku Deployment

**Prerequisites**: Heroku account

**Additional files needed**:
Create a `Procfile` in the project root:
```
web: sh setup.sh && streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

Create a `setup.sh` file:
```bash
mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
```

**Deployment steps**:
```bash
heroku create your-app-name
git push heroku main
```

### 3. Docker Deployment

**Build the image**:
```bash
docker build -t virgil-simulator .
```

**Run locally**:
```bash
docker run -p 8501:8501 virgil-simulator
```

**Deploy to cloud platforms**:
- **AWS**: Use ECS or Elastic Beanstalk
- **Google Cloud**: Use Cloud Run
- **Azure**: Use Container Instances

### 4. AWS EC2 Deployment

**Launch EC2 instance** (Ubuntu recommended):

1. **Connect to your instance** and install dependencies:
```bash
sudo apt update
sudo apt install python3 python3-pip git -y
```

2. **Clone and setup the project**:
```bash
git clone <your-repo-url>
cd virgil-financial-simulator
pip3 install -r requirements.txt
```

3. **Run the application**:
```bash
streamlit run app.py --server.port=8501 --server.address=0.0.0.0
```

4. **Configure security group** to allow inbound traffic on port 8501

5. **Optional: Setup PM2 for process management**:
```bash
npm install -g pm2
pm2 start "streamlit run app.py --server.port=8501 --server.address=0.0.0.0" --name virgil-simulator
```

## 🔧 Configuration Options

### Environment Variables

Set these environment variables for production deployments:

- `STREAMLIT_SERVER_PORT`: Port number (default: 8501)
- `STREAMLIT_SERVER_ADDRESS`: Server address (default: 0.0.0.0)
- `STREAMLIT_THEME_PRIMARY_COLOR`: Primary color for the theme

### Custom Domain Setup

For custom domains, you'll need to:

1. **Configure DNS** to point to your deployment
2. **Setup SSL certificates** (automatic with Streamlit Cloud/Heroku)
3. **Update security settings** as needed

## 🧪 Testing Before Deployment

**Run tests locally**:
```bash
python -m pytest test_app.py -v
```

**Test with scripts**:
```bash
./run.sh --test    # Linux/Mac
run.bat --test     # Windows
```

## 🚨 Troubleshooting

### Common Issues

1. **Module not found errors**
   - Solution: Ensure all dependencies are installed (`pip install -r requirements.txt`)

2. **Port already in use**
   - Solution: Change port with `streamlit run app.py --server.port=8502`

3. **Memory issues on cloud platforms**
   - Solution: Optimize the app or upgrade to a higher tier

4. **Slow performance**
   - Solution: Enable caching, optimize data processing

### Performance Optimization

1. **Add caching** to simulation calculations:
```python
@st.cache_data
def run_simulation_cached(*args):
    # Your simulation code here
    pass
```

2. **Use session state** for better user experience:
```python
if 'simulation_results' not in st.session_state:
    st.session_state.simulation_results = None
```

## 📊 Monitoring & Analytics

### Built-in Streamlit Analytics
- Streamlit Cloud provides basic usage analytics
- Monitor performance through the Streamlit Cloud dashboard

### Custom Analytics
Add Google Analytics or other tracking services by modifying the app configuration.

## 🔐 Security Considerations

1. **Environment Variables**: Store sensitive data in environment variables
2. **Authentication**: Add authentication for production use
3. **Rate Limiting**: Implement rate limiting for public deployments
4. **Input Validation**: Ensure all user inputs are properly validated

## 📱 Mobile Optimization

The app is responsive but for better mobile experience:
- Use `st.container()` for better layout control
- Optimize chart sizes for mobile screens
- Test on various device sizes

## 🎯 Production Checklist

- [ ] All tests pass locally
- [ ] Environment variables configured
- [ ] Security measures implemented
- [ ] Performance optimized
- [ ] Domain and SSL configured
- [ ] Monitoring setup
- [ ] Backup strategy in place
- [ ] Documentation updated

## 📞 Support

If you encounter deployment issues:
1. Check the troubleshooting section above
2. Review application logs
3. Open an issue in the GitHub repository
4. Contact the development team

---

**Happy Deploying! 🚀** 