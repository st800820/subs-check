name: Run subs-check daily at 6am

on:
  schedule:
    - cron: '22 22 * * *'  # UTC时间 22:22 = 北京时间 6:22（略微避开高峰）
  workflow_dispatch:       # 允许手动运行

jobs:
  subs-check:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'

    - name: Install dependencies
      run: |
        pip install -r requirements.txt

    - name: Run subs-check
      run: |
        python subs_check.py

    - name: Upload result to GitHub Pages
      run: |
        mkdir -p public
        cp -r output/* public/ || echo "No output to copy"
      continue-on-error: true

    - name: Deploy to GitHub Pages
      uses: peaceiris/actions-gh-pages@v4
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./public
