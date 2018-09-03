This readme details how to automate updating the stock database via launchd (Mac OS specific):

1. Copy com.stock.update.plist (stored in top directory of securities repo) to ~/Library/LaunchAgents/
2. Update the plist to point to your python interpreter (may not need to be changed) and cron_main.py directory
3. Load the plist job through the following command line: launchctl load ~/Library/LaunchAgents/com.stock.update.plist
4. Start the stock update plist job: launchctl start local.stock.update

NOTE: To see if the job has been loaded you can send the following command: launchctl list | grep stock.
      You should see output similar to this: -	0	local.stock.update
NOTE: More info on launchd here: http://www.launchd.info/