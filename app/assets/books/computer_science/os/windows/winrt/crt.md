## CRT - Microsoft C Runtime Library
Windows 10 Universal CRT
Windows OS component

- https://www.microsoft.com/en-us/download/details.aspx?id=50410
- https://docs.microsoft.com/fr-fr/cpp/windows/how-to-use-the-windows-10-sdk-in-a-windows-desktop-application?view=msvc-160
- [CRT - c-runtime-library](https://docs.microsoft.com/fr-fr/cpp/c-runtime-library/crt-library-features?view=msvc-160)

Prerequisites for Powershell

Visual Studio 2015 >= 
- La bibliothèque C Runtime (CRT) a été divisée en deux parties: 
    
    - UCRTBASE = Universal CRT = UCRT
    Contient les fonctions CRT standard C et propres à Microsoft que vous pouvez utiliser dans les applications Windows universelles. Cette bibliothèque est maintenant appelée Universal CRT, ou UCRT, et a été déplacée dans le kit de développement logiciel (SDK) Windows 10. Le UCRT contient de nombreuses nouvelles fonctions, telles que les fonctions C99, nécessaires pour prendre C++ en charge les normes de langage les plus récentes. 
    
    - VCRUNTIME
    Code de prise en charge, de démarrage et d’arrêt du runtime C
    Tout le reste qui n’a pas été placé dans le UCRT
    La bibliothèque vcruntime est installée avec le compilateur C++ et l’ensemble d’outils dans Visual Studio. 

Le UCRT est désormais un composant système qui est installé sur chaque version de Windows 10. Il est également disponible en tant que composant pouvant être installé pour toutes les versions antérieures de Windows prises en charge. Vous pouvez utiliser le kit de développement logiciel (SDK) Windows 10 pour cibler toutes les versions de Windows prises en charge. Pour obtenir la liste complète des systèmes d’exploitation pris en charge, consultez Windows 10 SDK.


Rust
    Safer alternative to C++ for low-level Windows programming. Rust is syntactically similar to C++ but has built-in protection against memory bugs that have long plagued developers working with the tricky and complicated C++. Thus Rust is sparking great interest in the .NET community
    
    Microsoft's Rust v0.9 provides full consumption support, meaning the language is now capable of calling ANY WINDOWS API. Done with a "LANGUAGE PROJECTION" (developers interact with Windows Runtime (WinRT) APIs in ways natural -- or idiomatic -- to specific languages).   
    Language projections:   
    - C++/WinRT
    - C#/WinRT
    - Rust/WinRT ["Rust for Windows"](https://github.com/microsoft/windows-rs)