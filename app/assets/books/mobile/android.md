# ANDROID


## Gradle
https://github.com/eskatos/gradle-command-action

https://medium.com/google-developer-experts/github-actions-for-android-developers-6b54c8a32f55


download.page(mobile/android_studio.md)
download.page(mobile/android_jetpack.md)

## more

- https://www.bogotobogo.com/Android/android25ActivityLifeCycle.php    and more...
- https://itnext.io/how-you-can-control-your-android-device-with-python-45c3ab15e260






# ANDROID

http://www.android.com/
https://www.freecodecamp.org/news/learn-to-develop-and-android-app-no-experience-required/  ***video
https://dev.to/educative/android-development-how-to-develop-an-android-app-c4g    *** to read
http://developer.android.com/sdk/index.html
https://dzone.com/articles/introduction-to-android-programming-using-the-andr
https://www.androidpit.fr/installer-drivers-android-adb-fastboot-windows#adb


*** https://zestedesavoir.com/tutoriels/624/creez-des-applications-pour-android/420_les-bases-indispensables-a-toute-application/2136_votre-premiere-application/


# May 2019: Google recommends Kotlin over Java.

# Flutter is a great cross-platform framework from Google that can be used to build applications for mobile, desktop, and web platforms. Officially released in December of 2018, it took barely a year to gain more popularity than React Native on both GitHub and Stack Overflow


https://developer.samsung.com/galaxy-themes


# Leader des systèmes d’exploitation de smartphones et tablettes en un temps record. Il est aujourd’hui le premier visé pour des développements d’applications mobiles et possède le plus grand magasin d’applications, devant l’App Store (Apple iPhone) et le Marketplace (Microsoft Windows Phone).


 SDK 	for writing applications using Java
 		SDK root 	C:\Users%user%\AppData\Local\Android\Sdk\tools\bin
 					C:\Users\nguin\AppData\Local\Android\Sdk → H:\android

 NDK 	for extending an SDK application with libraries written in C/C++
  	    set of additional tools that you can use to add native code to your android application

# AVD
	Android Emulator have some limitations compared to physical device. 
	Impossible to place or receive real phone calls, simulate USB connections, capture Camera / Video inputs, 
	use device-attached headphones or still use Bluetooth.

	https://developer.samsung.com/galaxy-emulator-skin/guide.html
	https://medium.com/@ssaurel/install-samsung-galaxy-s7-and-s7-edge-skins-in-your-android-emulator-846bbcd84d24

	To check the behaviour of your application on different kind of devices and configurations is essential. 
	With the tools offered by Google in the Android SDK, you can create virtual devices and define a lot specific 
	parameters to emulate different configurations. 
	For example, you can define screen size, resolution, RAM, internal memory or still sensors supported. 
	There are a lot of possibilities. 

	However, there is even a better feature offered by the Android Emulator. 
	You can define specific skins to change the aspect of your Android Emulator.

	2016: Samsung has released Android Emulator’s skins 
	
	Samsung Emulator Skins
		Emulator Skins are not just about looks. They give developers the closest possible experience to a real device.

	https://developer.samsung.com/galaxy-emulator-skin/overview.html	
		Download your preferred Galaxy Emulator Skin.
		Unzip in C:\Program Files\Android\Android Studio\plugins\android\lib\device-art-resources
		Extract the downloaded skin and copy it in Android Studio > plugins > android > lib > device-art-resources.
	Launch Android Studio and open AVD Manager (Tools > AVD Manager).
	Create Virtual Device
	New Hardware Profile
	Complete the fields with the specifications you would like to use
	In the Default Skin, select the downloaded Emulator Skin
	
	Galaxy S7, specifications to enter are the following :
		Screen Size : 5.1 inches
		Resolution : 1440 x 2560
		RAM : 4 GB
		Internal memory : 32/64 GB
		Card slot : microSD, up to 200 GB (dedicated slot)
		Hardware buttons : Yes
		Supported device states : Portrait and Landscape
		Cameras : Front and Back
		Sensors : Fingerprint, Accelerometer, Gyro, Proximity, Compass, Barometer, Heart Rate, SpO2


# INSTALL ANDROID

## Install Java SDK

	Install Android SDK

		. Android Studio android-studio bundle
		  http://developer.android.com/sdk/index.html
		  android-studio-bundle-135.1641136.exe

		or

		. stand-alone SDK Tools


				adt-bundle/sdk/platform-tools/ folder and the adt-bundle/sdk/tools/ folder to the end of your PATH variable:

	APACHE ANT
		Apache Ant is needed by Android and Cordova for building projects (with ionic for example)
		http://ant.apache.org/manual/install.html

## SDK Manager: Adding SDK Packages

# ANDROID SDK

	https://code.tutsplus.com/tutorials/understanding-the-android-app-development-kit--cms-34641

	Android apps are usually written in Java, C++, or Kotlin
	Android Development Tools
		Android Studio
		Android SDK
		Android SDK Platform Tools
		Android SDK Tools
		Android NDK

	Android Studio
		https://developer.android.com/studio
		Android Studio is a fully integrated, open-source development environment for the Android operating system, developed by Google. It offers a Gradle-based management system that provides greater flexibility in the build process.

### Android Studio comes with a fast emulator that allows you to install and run your apps faster on a virtual device and simulate different configurations and features. It also comes with Google Cloud Messaging, a feature that allows you to send push notifications to your apps.

		Android Studio's build system is powered by Gradle, which allows you to customize your build to generate multiple build variations for different devices from a single project. You can also view your app's CPU and memory network activity, identify performance bottlenecks, and see incoming and outgoing network payloads.

### Android Studio by Google has all the tools necessary for building apps on every type of Android device, and it's the official IDE for developing Android apps.

## Android software development kit (SDK)

		 development tools used to develop applications for the Android platform. 

		QEMU-based emulator 
		debugger
		required libraries
		documentation
		sample source code
		Android tutorials
		Supported development platforms include computers running on Windows, Linux, and macOS. 

	Android Platform Tools
	
		These tools support the features of the latest Android platform. It gets updated whenever a new SDK platform is installed. Each update of the platform tools is backward compatible with older platforms. 

		fastboot
		ADB

	Android SDK Tools
		
		included in Android Studio
		a component for the Android SDK
		complete set of development and debugging tools for Android.

		Android NDK
			The Android NDK is a companion toolset that lets you implement parts of your application in native code, using native languages such as C and C++. 
			For certain types of apps, this can help you reuse code libraries written in those languages, allowing you to incorporate features that would otherwise be impossible. 
			This means that your native code will be bundled into your application's .apk file and run on a virtual machine on the device.

### Some of the advantages of using native languages include:

		Ability to reuse code: NDK allows developers to use the same code written in C or C++ for different platforms in their Android application. 

### Faster Compiling: To convert Java or Kotlin code into machine-level code, you need to go to JVM, then JNI. NDK directly compiles the C or C++ code into machine-level language by generating a .so file without going through any intermediary process.

	What Is Android Debug Bridge (ADB)?
	
		ADB is a debugging tool used in the Android development environment. 
		It is a client-server program for performing a variety of device actions, such as installing and debugging apps. 
		It also provides access to a Unix shell for running commands. It includes the following three components:

		The client sends commands to the server.
		The daemon (the adbd) runs commands on a device.
		The server manages communication between the client and the daemon.
		ADB is included in the Android SDK Platform Tools package. You can download this package with the SDK Manager, which installs it at android_sdk/platform-tools. Or if you want the standalone Android SDK Platform Tools package, you can download it here.

# ENVIRONMENT VARIABLES


	JAVA_HOME	C:\Program Files\Java\jre1.8.0_25 			Add path to the Java SDK installation
	JAVA_HOME 	C:\Program Files\Java\jdk1.8.0_121
	JAVA_HOME 	C:\Program Files (x86)\Java\jre1.8.0_25

	set ANDROID_HOME=C:\<installation location>\android-sdk-windows
	set PATH=%PATH%;%ANDROID_HOME%\tools;%ANDROID_HOME%\platform-tools

	ANDROID_SDK_HOME is set to the root of your SDK: H:\android 
		This is the path of the preference folder expected by the Android tools. 
		It should NOT be set to the same as the root of your SDK. 
		Please set it to a different folder or do not set it at all. If this is not set we default to: C:\Users\nguin



	To find installation path: Keyboard Windows Button → Android SDK Tools → SDK Manager → Path is at the top of the window
	C:\Users\<user-name>\AppData\Local\Android\android-sdk
	set ANDROID_HOME=C:\Users\nicolas\AppData\Local\Android\android-sdk


	Set ANT_HOME to your bash profile:
	export ANT_HOME="$HOME/ant"
	export PATH="$PATH:$ANT_HOME/bin"

# Development on Android
	IDE Eclipse + plugin ADP
	IDE - Integrated Development Environment
	Android Studio


# PATHS

# C:\Users\nguin\AndroidStudioProjects
# C:\Users\nguin\AndroidStudioProjects\Tuto


# Move Android Studio AVD folder to a new location
	Default Android Virtual Device Manager (AVD) folder is located is in C:\Users\<user_name>\.android\avd. 
	To move it to a new location perform following steps:
	Close Android Studio
	Control Panel > System > Advanced System Settings > Environment Variables
	Add a new User variable:
	Variable Name: ANDROID_SDK_HOME
	Variable Value: D:\Android_SDK_HOME
	Replace D:\Android_SDK_HOME with the path you want become your new AVD folder root.
	The path you enter cannot be root folder of your Android SDK (but can be a subfolder).


# VARIABLES



# The ADB binary found at xxx is obsolete and has seriousperformance problems with the Android Emulator...
# Fix:
	Download ADB.exe (you can google it) and paste into this folder.
	C:\Users\siviw\AppData\Local\Android\Sdk\platform-tools\


# PHONE DEVELOPER MODE
		Settings → System → Developper options → USB debug + Stay active
		Settings → About → Android version (8.1.0)

	Android 9
		Settings → About → Software information → Numero de version 	type x7






# BASIC CONCEPTS
	
	* ACTIVITY
		kind of a window in which you place the UI components (texts, buttons...)
		single, standalone module of application functionality that usually correlates directly to a single user interface screen and its corresponding functionality.
	
	* INTENT
		The mechanism by which one activity is able to launch another and implement the flow through the activities that make up an application.
	
	* VIEW
		Items in a user interface such as the Button, CheckBox, RadioBox and so on, are subclasses of the Android View class. Views are also called widgets or components.
		Layout is a container view that is designed for controlling how child views are positioned on the screen. Some layouts are LinearLayout, TableLayout, RelativeLayout, GridLayout, CoordinatorLayout, ConstraintLayout, FrameLayout, etc. By default, Android Studio 3.0 will support the ConstraintLayOut.
	
	* RESOURCES
		contain resources such as the strings, images, fonts, and colors that appear in the user interface together with the XML representation of the user interface layouts. All of the text in a user interface is contained in resource files (default is strings.xml). This can be valuable when translating a user interface to a different spoken language.

# Keys

setContentView(R.layout.activity_main)

java
	\___ com.xxxxx
		MainActivity
res
  \___ layout
			activity_main.xml
			fragment_main.xml
  \___ values
  			strings.xml
				R.id
				<resources>
				    <string name="app_name">Tuto_12_Tabbed_Activity</string>
				    <string name="action_settings">Settings</string>
				    <string name="section_format">Hello World from section: %1$d</string>       ← string interpolation  
				</resources>


# 1st app
https://developer.android.com/training/basics/firstapp/creating-project


# How to Create an Android Application

	Android Studio 3.0
	Choose File > New > New Project
	Standard controls: Button, TextView, CheckBox, RadioButton, Plain Text...see Palette 
	activity_main.xml
		D&D a button at center...run...The button will be displayed in the upper left corner because we have not set up the constraint for the button
		To solve this problem, we click the white circles that appear around the button
		Warning: button text must be in resource..
		To solve this warning, we find and open the values folder and choose the strings.xml
		In activity_main.xml @string/nextpage in text attribute of the button
	Create the Second Activity
		Beside main activity, we can create other activities easily. The following steps will illustrate how to create the second activity:
		Right-click app, choose New > Activity > Empty Activity
		activity_second.xml 
			drag TextView from the Palette menu 
			In the strings.xml set a string resource
			In the text attribute in the Attributes window, typing @string/next_text



# Quick Start

# The steps below provide an overview of how to get started with the Android SDK. For detailed instructions, start with the Installing the SDK guide.

1. Prepare your development computer

# Read the System Requirements document and make sure that your development computer meets the hardware and software requirements for the Android SDK. Install any additional software needed before downloading the Android SDK. In particular, you may need to install the JDK (version 5 or 6 required) and Eclipse (version 3.4 or 3.5, needed only if you want develop using the ADT Plugin).

2. Download and install the SDK starter package

# Select a starter package from the table at the top of this page and download it to your development computer. To install the SDK, simply unpack the starter package to a safe location and then add the location to your PATH.

3. Install the ADT (Android Development Tools) Plugin for Eclipse

# If you are developing in Eclipse, set up a remote update site at https://dl-ssl.google.com/android/eclipse/. Install the Android Development Tools (ADT) Plugin, restart Eclipse, and set the "Android" preferences in Eclipse to point to the SDK install location. For detailed instructions, see ADT Plugin for Eclipse.

4. Add Android platforms and other components to your SDK

# Use the Android SDK and AVD Manager, included in the SDK starter package, to add one or more Android platforms (for example, Android 1.6 or Android 2.2) and other components to your SDK. If you aren´t sure what to add, see Which components do I need?

# To launch the Android SDK and AVD Manager on Windows, execute SDK Setup.exe, at the root of the SDK directory. On Mac OS X or Linux, execute the android tool in the <sdk>/tools/ folder. For detailed instructions, see Adding SDK Components.



http://androidforums.com

# WIDGETS



# APK (Android)
	Normalement, on installe un logiciel via le Google Play Store.
	Mais on peut aussi installer un paquet APK à la main.
	Pour l'installation d'un paquet APK sous Android, regardez : installer un fichier APK sur Android ?


# TUTORIALS

# 
[1. Interacting with the UI](https://proandroiddev.com/android-developer-beginner-step-1-interacting-with-the-ui-c7d2a793f2fa)

# MainActivity.kt  		Kotlin class, inheriting from the AppCompatActivity class

	Activity: kind of a window in which you place the UI components (texts, buttons...)
		Activity.onCreate() 	
			is called when the Activity is starting. 
			Where you make initialisations like binding the UI that you’ve created.

activity_main.xml 
	UI component 
		create them right in the code or you can do it in the XML 
		arranged by layouts
			[LinearLayout](https://developer.android.com/guide/topics/ui/layout/linear.html#Example)
			 	places views in one line (orientation=horizontal) - one after another
			 	places views in one column (orientation=vertical) - one after another
			[RelativeLayout](https://developer.android.com/guide/topics/ui/layout/relative.html)
			[FrameLayout](https://developer.android.com/reference/android/widget/FrameLayout.html)
			[ConstraintLayout](https://developer.android.com/reference/android/support/constraint/ConstraintLayout.html)

# Bind the layout with the Activity
 so we have the Activity class and we’ve created the UI in the XML file. The last thing to do is to bind the activity_main.xml file to our Activity
	Activity.setContentView(resourceId or view)

	 setContentView(R.layout.activity_main)

# Resources (res folder): "R" Class - R.id

	to manage them for the whole application project for different devices or configurations
	put there any resources like images, colors or strings...
	R class holds every resource id. For each type of resource, there is an R subclass (for example,R.drawable for all drawable resources), and for each resource of that type, there is a static integer (for example, R.drawable.icon). This integer is the resource ID that you can use to retrieve your resource.

	drawable 		R.drawable 		 R.drawable.icon
	layout
	mipmap
	values  		R.id.text_hello
	...

	create resources for different configurations
	Alt + Enter keys and choose “Extract string resource”.


# Manipulate views
	Activity.findViewById()

	 [Kotlin Android Extensions](https://kotlinlang.org/docs/tutorials/android-plugin.html) if we want to get rid of the Activity.findViewById()	 
     textView.setText("Hello, world!") // Instead of findViewById<TextView>(R.id.textView)

 Get user inputs
 	View.setOnClickListener()
 	View.OnClickListener

# Start another Activity
	Activity.startActivity(). The only parameter which we have to pass it’s a kind of intention 

	Add a new Activity
	The layout file will be created automatically and also the Activity will be added to the AndroidManifest.xml file.

[AndroidManifest.xml](https://developer.android.com/guide/topics/manifest/manifest-intro.html)

[2. Creating lists](https://medium.com/@mateuszbudzar/android-developer-beginner-step-2-lists-55c32aafce70)

two ways of implementing a list
# ListView
	 old UI component
	 https://medium.com/@mateuszbudzar/how-to-implement-a-listview-d5a2f718a7f1
# RecyclerView
	with Android Lollipop
	https://medium.com/@mateuszbudzar/how-to-implement-a-recyclerview-33fd4ff9988e

[3. Creating custom views]()

[4. Taking pictures]()

[5. Downloading data]()

[6. Storing data]()

[7. Make it delightful with Material Design]()



