
Performance and Troubleshooting
===============================

Troubleshooting connections
^^^^^^^^^^^^^^^^^^^^^^^^^^^


#. 
   ​Make sure you allow Pose Camera app to access the local network upon request. If you refused the first time, you may need to change this in your iphone Settings->Privacy->Local Network.

#. 
   As your phone needs to be allowed to speak to the demo application, make sure your firewalls (both desktop and potentially router) does not block the port (typically 8080 but can be set from the LiveLink menu or in the python code).

#. 
   Make sure your phone is on the same local network as the connecting computer (i.e. the one running Unreal Engine).

#. 
   For Unreal LiveLink, make sure UDP messaging is enabled. This can be done in Project Settings->Plugins->UDP Messaging->Enable Transport. This may require restarting your sources and/or application to take effect.

#. 
   Make sure you have entered the correct local IP address into the mobile app for the connecting machine (often in the form of 192.xxx.x.xxx using IPv4). For convenience the UE4 PoseAI plugin will show a local IP address in the LiveLink console and the python demo prints it to console. However, if you have multiple adapters this may not be your computer's hosting address so you may need to check network settings.

#. 
   On an IPv6 network try using the local-link address (starting with FE80: and, at least on our network, stopping before the % sign in the address)

Latency and Unreal LiveLink
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pose Camera can operate with very low latency, particularly on faster phones. Note that the speed of the machine running LiveLink can have a significant impact on the latency of the animation. On a "gaming" desktop, Unreal is able to process the incoming animations almost instantly, with little lag between real world action and on-screen movement. When tested using the same phone but instead paired with a laptop, without a dedicated GPU, significant lag of several hundred milliseconds was introduced.

LiveLink also includes several frames of buffering by default. For realtime applications this can create signficant delay. From the LiveLink menu select the PoseAI Source and in the details panel try reducing the buffering to a single frame.

Frames per second, heating and phone performance"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Better embedded chip hardware in newer phones can significantly improve the performance. Also, iPhones throttle the speed when the battery is worn or the phone runs hot.


* An iPhone 12 should routinely be able to process 60 camera frames per second into motion capture data for sustained periods of time.
* An iPhone 8 or X should be able to process 30 camera frames per second for sustained periods of time. For shorter times these phones can process approximately 50 out of the camera's 60 frames per second - however, the high computation load will likely cause the phone to heat up after a few minutes and the operating system is likely to throttle the speed of the app at some point to maintain a cooler temperature.
* While we do not officially support older phones, we have achieved 30 frames per second on a test iPhone 7, although some testers have reported their old phones struggled with the app.

Depending on use case, more camera frames is not always better. Aiming for a 30 frame per second rate, rather than 60, will save considerable computation and reduce battery drain and phone heating, and animations are often pruned to keyframes for memory efficiency. This can be configured through the LiveLink or python API.

If hand animations are unnecessary, use the body only modes to reduce computations (can be selected in LiveLink or configured in the Python handshake).

The app can stream at a user specified speed, interpolating the frames to deliver a smooth performance. For example, the user can capture at a 30 fps camera speed but stream interpolated motion capture data at 60 fps. However, higher streaming rates more heavily utilize the wireless chip on the phone. If interpolation is not necessary or is being handled on the paired application, consider reducing the stream rate to save battery and heating.

On older phones try turning off the camera preview once properly positioned (tap the yellow person icon at the edge of the screen). This may help reduce the strain on the phone.

Unreal Engine crashes
^^^^^^^^^^^^^^^^^^^^^

**Update 1.01 Live on Marketplace**

Some users reported an issue in some configurations where the engine would crash in the middle of a stream, usually with a message about TArray(Ftranforms)ResizeGrow. We could not consisitently replicate the issue but devised a small fix, that, at least on our systems, eliminated even the occasional crash.

To upgrade to the latest version of the plugin, click under your Engine Version from the Epic Games Unreal launcher, where it says "Installed Plugins!", and then click update next to our plugin.

As we are made aware of other issues we will try to address them. Do please let us know if you are suffering from any other Unreal Engine crashes regularly related to our plugin as we do not get told by Epic Games when you submit a report to them.
