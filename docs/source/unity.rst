
Adding PoseAI input to Unity
============================

Copy the PoseAI UnityAPI files
------------------------------

Download and copy the PoseAI UnityAPI folder of scripts into your project's Assets folder

Disable redundant controllers on the PlayerArmature
---------------------------------------------------

Select the PlayerArmature in the sample project and disable or delete the AnimationController, ThirdPersonCharacterController, and PlayerInput controllers.

We will replace the functionality of these controllers with the PoseAI controllers, and disablling them prevents two sets of controls being sent to the character.

Make sure to keep the CharacterController component, as we will use that for player movement.

Add a PoseAI SourceDirect component to the armature
---------------------------------------------------

Select the Player Armature, click on Add Component and add a PoseAI SourceDirect component to the armature.

This component sets up a UDP server to communicate with the Pose Camera app. Each source needs to be on its own port, and you can have multiple players connect to different sources. Character objects can share sources by using a PoseAI SourceShared component, many of which can be pointed at a particular PoseAI SourceDirect component.

Make sure the Rig Type is set to Unity for the Sample project mesh. We also provide preconfigured rigs for other common options (for example most newer Mixamo rigs).

The *Mode* should be set to either *Room* or *Portrait*. For Room mode you will film from your phone in landscape orientation and capture a wider space, although you need to back further away to be fully in the frame. For Portrait mode, you will film from portrait orientation. This allows you to be closer, helpful in smaller rooms, but means you can't capture much lateral movement.

Add the PoseAI AnimatorComponent
--------------------------------

Select the Armature again and click on Add Component. This component allows you to use live player input to animate the character.

*AnimationAlpha* allows you to blend between conventional animations and the live motion capture. The script automatically blend back to zero when the camera can't find a subject.

*UseUpperBodyOnly* only animates the upper body and works well when combined with the PoseAI CharacterController. This combines the standard state machine animation for the lower body, triggered by input events, with the player's upper body live motion capture. This should be set to True for this demo.

*MoveRootSideways* moves the root in response the live capture movement in the camera frame (i.e. if the player moves side to side). This should be on if you are using full body animation and also not using the CharacterController. A use case would be showing a dance move on screen.

Enable IK Pass on the Animator asset
------------------------------------

Our animation component uses the IK input functions to override the standard animations, while allowing easy blending.

Make sure the animator component points to the Starter Assets Third Person (Animator Controller). Open the component, click on the gear symbol in the base layer and enable the "IK Pass".

Add the PoseAICharacterController
---------------------------------

Select the PlayerArmature again and Add Component. This controller is similar to the starter controller but instead of using keyboard/mouse input, it uses motion capture input to move the character.

There are a lot of configuration options but we suggest trying the default settings first. We start by enabling multiple ways to trigger movement, but this can be configured through defaults or in the script.

* You can lean to the side or twist your upper body to have your character rotate.
* While the character is on the ground, you can jog in place and/or pump your arms up and down to move forward. Depending on how fast you jog or pump, you will either walk forward or sprint forward
* If you want to fly, flap your arms or do chest expansions. Holding your arms out (i.e. T-position) will put you in glide mode, slowing your fall but giving you forward speed. Bring your arms back to your sides to plummet. You can still lean or twist to bank into turns.
* Jump in RL to jump in game
* Crouching in RL is picked up but the starter animation pack does not include crouching so currently it only creates a text output in console.

Connect Pose Camera on your phone
---------------------------------

Open the PoseCamera app on your phone. Go to settings (gear icon):


.. image:: https://static.wixstatic.com/media/9e8b9f_1e61a2749213404f9a25325d6dc5a061~mv2.jpg =x600
   :target: https://static.wixstatic.com/media/9e8b9f_1e61a2749213404f9a25325d6dc5a061~mv2.jpg =x600
   :alt: 


and input the IP address of the computer running the Unreal Engine:


.. image:: https://static.wixstatic.com/media/9e8b9f_062bdd65dd7b443bb2d0f4637433810e~mv2.jpg =x600
   :target: https://static.wixstatic.com/media/9e8b9f_062bdd65dd7b443bb2d0f4637433810e~mv2.jpg =x600
   :alt: 

This can usually be found displayed in LiveLink (but if you have multiple adapters this may not be correct). **Make sure your phone and the computer are on the same local network.**

Close settings on your phone. The app should show the IP address you entered at the bottom of the main screen. You may be asked to rotate your phone sideways:


.. image:: https://static.wixstatic.com/media/9e8b9f_91c61f9a691c4d7c8b8a869dee03737b~mv2.jpg =x600
   :target: https://static.wixstatic.com/media/9e8b9f_91c61f9a691c4d7c8b8a869dee03737b~mv2.jpg =x600
   :alt: 



.. image:: https://static.wixstatic.com/media/9e8b9f_f45ee5d084c14942835e3c033fc12745~mv2.jpg =600x
   :target: https://static.wixstatic.com/media/9e8b9f_f45ee5d084c14942835e3c033fc12745~mv2.jpg =600x
   :alt: 

Tap to connect. When successful connected the phone app should display "Unreal LiveLink" in place of the IP address, and say "tap to stream". Tap to begin the stream and the app will switch to camera mode.

Unsuccessful? Try our troubleshooting page for tips resolving common connection issues
