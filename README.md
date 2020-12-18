# SOE-ProgAlap1-Beadando-Kebelei-Csaba
A program egy egyszerű játékot valósít meg. Induláskor egy menüvel tudjuk irányítani a program futását. A menüpontok után egy bementet vár a szoftver, ami lehet 1, 2, 3. A következő menüpontokat láthatjuk:

    [1] Snake játék indítása 🐍
    [2] Eredmények megnézése 🏆
    [3] Kilépés a játékból ❌

<ol>
<h2><li>Snake játék indítása 🐍</h2>
<p> A legelső menüpont a játékot indítja el, ami indulás előtt egy nickname-et, becenevet vár, ami nem lehet hosszabb 16 karakternél. A játék célja, hogy minnél több pontot szerezzünk. A pontszám növekedését úgy érjük el, hogy ha a kígyó megeszik egy π karaktert, ami a pályán véletlenszerűen jelenik meg. Az étkezés után lehetőség van még repetázni, mert a pályán újra megjelnik egy π karakter. A kígyót úgy tudjuk etetni, hogy a π-re irányítjuk, amit a billentyűzet nyilaival tudunk megtenni. Minden elfogyasztott π után megnő a kígyó hossza, ami nehezíteni fogja a játékunk, mivel így könyebben irányíthatjuk a fejét a saját testébe, és ennek a következménye a játék vége. Ezen kívül még el kell kerülnünk azt, hogy a pálya falához érjünk, mert szintúgy vége lesz a játékunknak. Az eredményünk mentésre kerül, amiről tájékoztatást kapunk:</p>

![](https://github.com/Teaching-projects/SOE-ProgAlap1-Beadando-Kebelei-Csaba/blob/master/gameplay.jpg)

    'Nickname', a te pontszámod 7 és ezt eredményed elmentettük. 😁

<p>Ilyenkor viszajutunk az eredeti állapothoz és menü lesz újra előttünk.</p></li>
<h2><li>Eredmények megnézése 🏆</h2>
<p>A második menüpont az elmentett eredményekről tájékoztat a következő formában:</p>

    Eredmény         Nickname          Dátum             Pontszám
       🥇            Petike            2020-12-12        16
       🥈            'Nickname'        2020-12-13        7
       🥈            Jóska             2020-12-13        7
       🥉            Jácint            2020-12-12        6

<p>Az első három legjobb eredmény jelenítődik meg, illetve, ha holtverseny alakult ki a az eredmények között, akkor az adott helyezéssel több eredmény is megjelenik. Viszont ha nincs még egy eredmény se akkor arról a következő üzenetbe tájékozódhatunk:</p>

    Eredmény         Nickname          Dátum             Pontszám
    Nincs adatunk... Még játszani kell. 😉
</li>

<h2><li>Kilépés a játékból ❌</h2>
<p>A harmadik menüpont segítségével tudjuk bezárni a programot, vagyis a program futásának ezzel véget vethetünk.</p>