 //dias habilitados entre 2022-2023
    //janeiro  
    let d1 = toDate("01/02/2022"),
    d2 = toDate("01/01/2023"),
    intervalos = [];

    intervalos.push( toString(d1) );

    while ( d1 < d2 ) {
    d1.setDate( d1.getDate() + 1 );
    intervalos.push( toString(d1) );
    }
    function toDate(texto) {
        let partes = texto.split('/');
        return new Date(partes[2], partes[1]-1, partes[0]);
    }

    function toString(date) {
        return ('0' + date.getDate()).slice(-2) + '/' +
        ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
        date.getFullYear();
    }
    //fevereiro
    let d3 = toDate("01/03/2022"),
    d4 = toDate("01/02/2023"),
    intervalos1 = [];

    intervalos1.push( toString(d3) );

    while ( d3 < d4 ) {
    d3.setDate( d3.getDate() + 1 );
    intervalos1.push( toString(d3) );
    }
    function toDate(texto) {
        let partes = texto.split('/');
        return new Date(partes[2], partes[1]-1, partes[0]);
    }

    function toString(date) {
        return ('0' + date.getDate()).slice(-2) + '/' +
        ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
        date.getFullYear();
    } 
    
    //março
    let d5 = toDate("01/04/2022"),
    d6 = toDate("01/03/2023"),
    intervalos2 = [];

    intervalos2.push( toString(d5) );

    while ( d5 < d6 ) {
    d5.setDate( d5.getDate() + 1 );
    intervalos2.push( toString(d5) );
    }
    function toDate(texto) {
        let partes = texto.split('/');
        return new Date(partes[2], partes[1]-1, partes[0]);
    }

    function toString(date) {
        return ('0' + date.getDate()).slice(-2) + '/' +
        ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
        date.getFullYear();
    }

    //abril
    let d7 = toDate("01/02/2022"),
    d8 = toDate("01/01/2023"),
    intervalos3 = [];

    intervalos3.push( toString(d7) );

    while ( d7 < d8 ) {
    d7.setDate( d7.getDate() + 1 );
    intervalos3.push( toString(d7) );
    }
    function toDate(texto) {
        let partes = texto.split('/');
        return new Date(partes[2], partes[1]-1, partes[0]);
    }

    function toString(date) {
        return ('0' + date.getDate()).slice(-2) + '/' +
        ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
        date.getFullYear();
    }
    //maio
    let d9 = toDate("01/03/2022"),
    d10 = toDate("01/02/2023"),
    intervalos4 = [];

    intervalos4.push( toString(d9) );

    while ( d9 < d10 ) {
    d9.setDate( d9.getDate() + 1 );
    intervalos4.push( toString(d9) );
    }
    function toDate(texto) {
        let partes = texto.split('/');
        return new Date(partes[2], partes[1]-1, partes[0]);
    }

    function toString(date) {
        return ('0' + date.getDate()).slice(-2) + '/' +
        ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
        date.getFullYear();
    } 
    
    //junho
    let d11 = toDate("01/04/2022"),
    d12 = toDate("01/03/2023"),
    intervalos5 = [];

    intervalos5.push( toString(d11) );

    while ( d11 < d12 ) {
    d11.setDate( d11.getDate() + 1 );
    intervalos5.push( toString(d11) );
    }
    function toDate(texto) {
        let partes = texto.split('/');
        return new Date(partes[2], partes[1]-1, partes[0]);
    }

    function toString(date) {
        return ('0' + date.getDate()).slice(-2) + '/' +
        ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
        date.getFullYear();
    } 

    //junho
    /*
    let d13 = toDate("01/04/2022"),
    d14 = toDate("01/03/2023"),
    intervalos6 = [];

    intervalos6.push( toString(d11) );

    while ( d13 < d14 ) {
    d13.setDate( d13.getDate() + 1 );
    intervalos6.push( toString(d13) );
    }
    function toDate(texto) {
        let partes = texto.split('/');
        return new Date(partes[2], partes[1]-1, partes[0]);
    }

    function toString(date) {
        return ('0' + date.getDate()).slice(-2) + '/' +
        ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
        date.getFullYear();
    } 

    */
    //julho
    /*
    let d15 = toDate("01/04/2022"),
    d16 = toDate("01/03/2023"),
    intervalos6 = [];

    intervalos6.push( toString(d15) );

    while ( d15 < d16 ) {
    d15.setDate( d15.getDate() + 1 );
    intervalos5.push( toString(d15) );
    }
    function toDate(texto) {
        let partes = texto.split('/');
        return new Date(partes[2], partes[1]-1, partes[0]);
    }

    function toString(date) {
        return ('0' + date.getDate()).slice(-2) + '/' +
        ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
        date.getFullYear();
    } 

    */
    //agosto
    /*
    let d11 = toDate("01/04/2022"),
    d12 = toDate("01/03/2023"),
    intervalos5 = [];

    intervalos5.push( toString(d11) );

    while ( d11 < d12 ) {
    d5.setDate( d5.getDate() + 1 );
    intervalos5.push( toString(d11) );
    }
    function toDate(texto) {
        let partes = texto.split('/');
        return new Date(partes[2], partes[1]-1, partes[0]);
    }

    function toString(date) {
        return ('0' + date.getDate()).slice(-2) + '/' +
        ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
        date.getFullYear();
    } 

    */
    //setembro
    /*
    let d11 = toDate("01/04/2022"),
    d12 = toDate("01/03/2023"),
    intervalos5 = [];

    intervalos5.push( toString(d11) );

    while ( d11 < d12 ) {
    d5.setDate( d5.getDate() + 1 );
    intervalos5.push( toString(d11) );
    }
    function toDate(texto) {
        let partes = texto.split('/');
        return new Date(partes[2], partes[1]-1, partes[0]);
    }

    function toString(date) {
        return ('0' + date.getDate()).slice(-2) + '/' +
        ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
        date.getFullYear();
    } 

    */
    //outubro
    /*
    let d11 = toDate("01/04/2022"),
    d12 = toDate("01/03/2023"),
    intervalos5 = [];

    intervalos5.push( toString(d11) );

    while ( d11 < d12 ) {
    d5.setDate( d5.getDate() + 1 );
    intervalos5.push( toString(d11) );
    }
    function toDate(texto) {
        let partes = texto.split('/');
        return new Date(partes[2], partes[1]-1, partes[0]);
    }

    function toString(date) {
        return ('0' + date.getDate()).slice(-2) + '/' +
        ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
        date.getFullYear();
    } 

    */
    //novembro
    /*
    let d11 = toDate("01/04/2022"),
    d12 = toDate("01/03/2023"),
    intervalos5 = [];

    intervalos5.push( toString(d11) );

    while ( d11 < d12 ) {
    d5.setDate( d5.getDate() + 1 );
    intervalos5.push( toString(d11) );
    }
    function toDate(texto) {
        let partes = texto.split('/');
        return new Date(partes[2], partes[1]-1, partes[0]);
    }

    function toString(date) {
        return ('0' + date.getDate()).slice(-2) + '/' +
        ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
        date.getFullYear();
    } 

    */
    //dezembro
    /*
    let d11 = toDate("01/04/2022"),
    d12 = toDate("01/03/2023"),
    intervalos5 = [];

    intervalos5.push( toString(d11) );

    while ( d11 < d12 ) {
    d5.setDate( d5.getDate() + 1 );
    intervalos5.push( toString(d11) );
    }
    function toDate(texto) {
        let partes = texto.split('/');
        return new Date(partes[2], partes[1]-1, partes[0]);
    }

    function toString(date) {
        return ('0' + date.getDate()).slice(-2) + '/' +
        ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
        date.getFullYear();
    } 

    */
   