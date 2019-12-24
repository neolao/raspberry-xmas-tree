Raspberry xmas tree
===================

Install
-------
```bash
sudo apt-get install python-pip python-gpiozero python3-gpiozero
pip install statistics
```

Run at startup
--------------
```bash
sudo ln -s $(pwd)/xmas-tree.service /etc/systemd/system/xmas-tree.service
sudo systemctl enable xmas-tree.service
sudo systemctl start xmas-tree.service
```
