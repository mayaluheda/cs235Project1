# tiktok-noise-control-experiment

CS315 project testing how age affect a user's recommendation algorithm using Selenium.

By: Tayae Rogers, Sophie Hwang, Catherine Foster, Jenni Yu, Maya Lu-Heda, Jasmine Khuu

Credits: CS315 Project 1 Section 2 Group 2

Instructions for running:
1. First clone the repository on VSCode and set up a Python virtual environment.
2. Install the required packages: pip install -r requirements.txt
3. Open TWO terminals on vscode and split it for better view
4. Run this command first for the active user:
python -m pytest tests/tiktok/test_active.py --html=report_active.html
3. Login with your active tiktok user.
4. Go back to the vscode terminal. Run this command on the other terminal for the control user:
python -m pytest tests/tiktok/test_control.py --html=report_control.html
5. Login with your control tiktok user.
6. Now just wait!
