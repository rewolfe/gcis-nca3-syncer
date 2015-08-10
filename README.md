# gcis-nca3-syncer
Syncer script to update a GCIS endpoint with missing NCA3 figures, datasets, etc.

Install
-------

1. Install:
 ```
 $ ./install.sh
 ```

1. Ensure you've set up GCIS credentials in $HOME/etc/Gcis.conf:
 ```
 $ cat ~/etc/Gcis.conf
 ---
 - url      : https://localhost:3000
   userinfo : gmanipon:<GCIS API key>
   key      : <GCIS API key>
 ```

1. Make sure GCIS web app is running.


Updated Figure 9.3 - Wildfire Smoke has Widespread Health Effects
-----------------------------------------------------------------
```
$ ./update_figure-9-3.sh https://localhost:3000
```
