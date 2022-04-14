.. role:: raw-html-m2r(raw)
   :format: html


Frequently Asked Questions
==========================

What are the different modes?
-----------------------------

Pose Camera offers different camera/AI modes optimized for various situations.  This helps maintain low latency on even mid-range phones, as targetted algorithims are quicker and smaller.  The mode is automatically set by the paired program


* Room Mode: for standing interaction and movement in a normal sized living room.  Full body capture from a few meters away.  Great for dance moves.
* Desktop Mode: for upper body interaction while seated at a desk.  Great for hand gesture interaction.
* Portrait Mode: for full body interaction with little lateral movement, useable in tighter spaces.

We also intend to add further modes in the future, such as:


* Floor Mode - for exercises and poses while laying down.
* Martial Arts Mode - AI specifically targetted for rapid martial arts
* Swing Mode - AI specifically targetted for racquet and golf swings.

Does Pose Camera stream my camera feed?  What about privacy?
------------------------------------------------------------

No, our AI runs fully on the phone, no server necessary.  We thought users might be uncomfortable with the idea of streaming their camera feed to a server, so we process it all on device.  Our software converts images into a stream of skeletal animation - basically a bunch of angles between connected bones.  The user choses where to send the animation stream, usually  a game, app or engine on their local network.

Can I use Pose Camera to record animations?
-------------------------------------------

Pose Camera streams skeletal animations estimated from the camera feed.  It has no built-in recording capability and is meant to be used in conjuction with other software.

You can use our free Unreal Engine LiveLink plugin to receive that stream and use some of the many tools Unreal provides, such as the "Take Recorder", to record and edit the animation.   Our steam them to Python (see our example) and use them with a 3D modelling suite.  

You are then free to use those animations however you want - our only condition is you do not use them to reverse engineer our software, build databases for AI research or for testing and training AI models.

Can I use videos instead of the live camera feed?
-------------------------------------------------

We currently do not include an option to use existing videos rather than the live camera. However, you can certainly get solid results aiming the phone camera at another screen playing a video at a high resolution

How realtime is Pose Camera?
----------------------------

Our software is designed for low-latency game ready motion control input.  We redesigned our research AI to perform quickly on the more limited resources of even mid-range phones.

We also avoid roundtrip internet latency by processing everything on the phone.  

This latency also depends on the hardware - newer phones are obviously faster than older phones.  Some phone cameras and OS's introduce a small internal processing lag as well. 

You should expect 20-100ms of latency between real world action and in-game reaction.

Note for UE4 LiveLink Users: the speed of the machine running Unreal and LiveLink can have a significant impact on how quickly Unreal can process the incoming animations and display in editor or on screen. 

Will running motion capture slow my game?
-----------------------------------------

Our AI does not use desktop / console resources.  Our software is targetted toward providing input into game engines and fitness apps.  Often these apps need all the hardware power available to provide bleeding edge graphical experiences.  We did not want to compete with resources by running our AI on the desktop or console.  We run our AI algorithms on the hardward embedded in the phone, perserving desktop or console CPU/GPU cycles for the exclusive use of game developers.

How does Pose Camera compare to other Mocap systems?
----------------------------------------------------

Pose Camera is designed to accessibly provide motion input without special hardware, using only a smartphone and its normal camera feed.   Strapping on a mocap suit or using eight depth-sensing cameras will likely provide more accurate input.\ :raw-html-m2r:`<br>`
Pose Camera is also designed to provide live motion input.  Systems which process a complete session afterwards can allow more robust smoothing techniques and error correction.
Pose Camera AI runs fully on the phone, in real-time.  We stripped down our powerful state-of-the-art research model to provide the best balance of speed and accuracy.  Other systems which process on a server or workstation can run larger, more computationally and memory expensive models which may provide higher accuracy or recognize more unusual poses.  

Why doesn't my character's hands meet like that of my mocap subject?
--------------------------------------------------------------------

If you are animating a character with different body proportions compared to the target of Pose Camera, this is expected.  Pose Camera captures the joint angles of the target.  A subject with longer arms would need to rotate less to reach a point across the body, and a subject with shorter arms would need to rotate more.

As Pose Camera has no knowledge of the character animation, this would need to be handled by the animation software, or by using a similarly sized character.

Why does Pose Camera work better on some movements and poses?
-------------------------------------------------------------

Running pose estimation in realtime on a mobile phone requires considerable optimization.  Our initial release focuses on common movements, whether upright for Room mode or seated for Desktop.  For this release we have not trained our AI on unusual positions particular to certain sports or activities.

Over time we plan on releasing additional modes tailored to specific activities and providing more accurate motion capture in different use cases.

Does Pose Camera track root motion (i.e. target movement in real space)?
------------------------------------------------------------------------

Our AI mainly focuses on estimating joint rotations for an animation skeleton.  We also estimate vertical and lateral movement in the camera frame, and this can be seen with root character motion in the UE4 LiveLink plugin.  At this time we do not estimate depth movement (i.e. movement closer or further to the camera).  

Moving the camera during streaming can add considerable noise to the root movement.

Is your AI open source? Where does it come from?
------------------------------------------------

We initially developed our pose estimation AI at Imperial College London in 2019.  Our innovative approach delivered state-of-the-art accuracy, significanllty improving upon the benchmarks in other published research.  Since then we have worked hard to migrate our academic research into production, and from high powered servers into lightweight phones.

We have not made our algorithm open source and the core of our technique is currently patent pending. 

Will you also release on Android?
---------------------------------

We hope so!  Our software pipeline was designed to eventually allow deployment on multiple platforms and to work on a wide range of phones, not just the newest iPhone.  We will keep our user base updated as we progress on this front.
