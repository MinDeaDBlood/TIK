##  TIK
####  **Введение* 
***
> [!Осторожно]
> Этот проект не опубликован в gitcode. Если вы найдете этот проект в gitcode, пожалуйста, свяжитесь с нами и сохраните скриншот, подтверждающий это.
***
> [!Осторожно]
> Свободное программное обеспечение, коммерческое использование которого запрещено без разрешения

1.  【 **Программа TIK** 】 —— Программа для работы с прошивками, с открытым исходным кодом, поддерживающая обработку всех образов прошивок Android, в настоящее время обновлена до Ver.5；

2. Разбирает и собирает наиболее распространенные образы, а также поддерживает разделы erofs/V-AB

3. Новая функция - настройка привычек, взаимодействия и поведения при сборке (упаковке)

4. Поддерживает Android 15

5. Совершенно новое решение MKC_Boot_Kitchen[boot|exaid|recovery/etc].img
    
6. Полная поддержка super.img и динамических типов разделов (V-AB). Правильно определяет разделы и образы находящиеся внутри super.img (V-AB), разбирает их и собирает обратно. Поддерживает различные способы сборки образа (упаковки) - (полуавтоматическое распознавание, эффективное и стабильное)

####  **Возможности программы** 

【 **Определение, распаковка и упаковка** 】

1. 【 *.zip, *.br, *.dat, ext4/2 *.img, bootimg и т.д.】- определяет, разбирает и собирает образы
2. 【 Super.img <A-onloy/AB/V-AB>, bootimg<header3>, erofs *.img,  F2FS(Эта программа поддерживает 64-разрядную версию LINUX) и т.д.】 Определяет, разбирает и собирает самые новые образы
3. 【 dtbo，dtb , TWRP, ops, ofp, ozip, payload.bin, *.win000-004, *.dat.1~20 и т.д.】- Разбирает и собирает нестандартные типы файлов
4. Идеально адаптирован к последней версии **Android 14** **Erofs** **Динамическим разделам** **Типам разделов V-AB**


【 **Поддерживаемая архитектура** 】

1. Телефонный Termux  Arm64[aarch64] встроенная поддержка или [<Linux Deploy>/Termux] Chroot Ubuntu 20.04 и выше Arm64[aarch64] 【Для повышения эффективности рекомендуется использовать Chroot】

2. Виртуальная машина или физическая машина Ubuntu 20.04 и выше x86_64[x64]

3.Windows 7 и выше [x64/x86]

Note: У WSL может быть проблема с неправильными разрешениями, проверьте ее на свое усмотрение!
#### **Ссылки на проекты, которые были использованы для создания данной программы**
1. [ApkParse](https://github.com/zxvzxv/ApkParse/)
2. [sdat2img](https://github.com/xpirt/sdat2img)
3. [img2sdat](https://github.com/xpirt/img2sdat)
4. [make_ext4fs](https://github.com/jamflux/make_ext4fs)
5. [oppo_decrypt](https://github.com/bkerler/oppo_decrypt)
6. [lpunpack](https://github.com/unix3dgforce/lpunpack)
7. [brotli](https://github.com/google/brotli)
8. [rich](https://github.com/Textualize/rich/)
9. [context_patch](https://github.com/ColdWindScholar/context_patch)
10. [erofs-utils](https://github.com/sekaiacg/erofs-utils/)
11. [Magisk_Patch_Python](https://github.com/ColdWindScholar/Magisk_Patch_Python)
12. И многое другое...
#### **Поддержавшие развитие проекта**
1. Sakura
2. Affggh
3. Yeliqin666
4. [qlenlen - For F2FS REPACK](https://github.com/qlenlen)
5. Перевод и адаптация на русский: Rayne Kobatashi (https://github.com/MinDeaDBlood)
#### **Поддерживаемые ОС**
1. Android-(Termux) | ARM64
2. Windows 7 и новее | AMD64 X86 ARM64
3. Linux | ARM64 X86_64
4. Macos | ARM64 X86_64
####  **Руководство по установке** 

    git clone https://github.com/ColdWindScholar/TIK
    cd TIK
    chmod a+x ./*
    python build.py
    sudo ./run

#### **Инструкция по применению** 

1.  Попробуйте выполнить все операции в Termux【 **Предупреждение **** Не используйте системный root ** 】, ПК потребуются права Root (sudo, на самом деле, вам не нужен) и лучше всего не запускать этот инструмент от имени 【суперпользователя】, чтобы избежать проблем с разрешениями при подключении к телефону после сборки!
2.   **О выборе файлов в Proot**  
    - -Пожалуйста, поместите zip-файл или подключаемый модуль mpk в 【** В папку программы**】, программа автоматически найдет его (вы можете изменить это в настройках).

3.  Папка программы в телефонном терминале termux proot в ubuntu:【**/data/data/com.termux/files/home/ubuntu/root/TIK**】

4.  **Пожалуйста, не удаляйте【папку проекта/папку конфигурации】. Информация о файле, необходимая для сборки, находится здесь. Программа автоматически изменит размер в соответствии с динамическим разделом!(Можно настроить самостоятельно)

5.  Из-за производительности мобильного телефона, эффективности proot, режима работы (** автоматического сравнения fs_config перед сборкой img, не будет собран сразу**) и других причин, возможны задержки при работе, наберитесь терпения, просто подождите некоторое время;

6. Попробуйте удалить файлы в 【Termux или proot ubuntu】, выполните 【rm -rf файл, папка】【**Не используйте системный рут** 】

7.   **Для обеспечения нормальной работы программы, пожалуйста, соблюдайте строгие условия: рабочий путь не должен содержать китайских иероглифов или пробелов, в папке проекта не должно быть пробелов или других специальных символов, а имя файла не должно быть слишком длинным！！！** 

8.   **Динамические разделы не позволяют выполнить однократную прошивку любого раздела из этих разделов (кроме случаев, когда используется fastbootd), пожалуйста, обратитесь к документации Android для получения подробной информации** 

9. При использовании программы на мобильном телефоне, если вы используете ** СИСТЕМНЫЙ ROOT ** для выполнения операций в папке проекта (таких как: ** Добавление файлов, изменение файлов**), пожалуйста, не забудьте предоставить файлам или папке полные права - **777**！！！

10. **Автоматическое создание образа - в один клик*：У отдельных производителей есть ограничения на некоторые разделы, и в настоящее время рекомендуется использовать режим fastbootd для сохранения целостности информации Super раздела.


#### **Участие в каналах поддержки**

 Пожалуйста, инициируйте PR, и мы проверим и обработаем его как можно скорее. Спасибо всем разработчикам/энтузиастам, которые поддерживают этот проект!


#### **Обмен отзывами**

  Группа в QQ：[932388310](#交流反馈)

#### **Отказ от ответственности** 

1.   Эта программа работает в среде Termux proot и не требует прав суперпользователя 【 **Пожалуйста, внимательно используйте системный root в Termux** 】 ！！！

2.  Эта программа не содержит незаконного кода, такого как:【разрушение системы, кража данных】как и других незаконных кодов ！！！

3.  **Если данные будут утеряны или повреждены из-за использования пользователем прав суперпользователя для работы с папками проектов в программе, мы не несем за это ответственность！！！** 
####  [TIK5.0](https://github.com/ColdWindScholar/TIK) 
#### ColdWindScholar(3590361911@qq.com).Все права защищены.
