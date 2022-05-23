 //dias habilitados entre 2022-2023
    //janeiro  
    let d1 = toDate("01/01/2022"),
    d2 = toDate("31/01/2022"),
    intervalos1 = [];

    intervalos1.push( toString(d1) );

    while ( d1 < d2 ) {
    d1.setDate( d1.getDate() + 1 );
    intervalos1.push( toString(d1) );
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
    let d3 = toDate("01/02/2022"),
    d4 = toDate("28/02/2022"),
    intervalos2 = [];

    intervalos2.push( toString(d3) );

    while ( d3 < d4 ) {
    d3.setDate( d3.getDate() + 1 );
    intervalos2.push( toString(d3) );
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
    let d5 = toDate("01/03/2022"),
    d6 = toDate("31/03/2022"),
    intervalos3 = [];

    intervalos3.push( toString(d5) );

    while ( d5 < d6 ) {
    d5.setDate( d5.getDate() + 1 );
    intervalos3.push( toString(d5) );
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
    let d7 = toDate("01/04/2022"),
    d8 = toDate("30/04/2022"),
    intervalos4 = [];

    intervalos4.push( toString(d7) );

    while ( d7 < d8 ) {
    d7.setDate( d7.getDate() + 1 );
    intervalos4.push( toString(d7) );
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
    let d9 = toDate("01/05/2022"),
    d10 = toDate("31/05/2022"),
    intervalos5 = [];

    intervalos5.push( toString(d9) );

    while ( d9 < d10 ) {
    d9.setDate( d9.getDate() + 1 );
    intervalos5.push( toString(d9) );
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
    let d11 = toDate("01/06/2022"),
    d12 = toDate("30/06/2022"),
    intervalos6 = [];

    intervalos6.push( toString(d11) );

    while ( d11 < d12 ) {
    d11.setDate( d11.getDate() + 1 );
    intervalos6.push( toString(d11) );
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

    //julho
    
    let d13 = toDate("01/07/2022"),
    d14 = toDate("31/07/2022"),
    intervalos7 = [];

    intervalos7.push( toString(d13) );

    while ( d13 < d14 ) {
    d13.setDate( d13.getDate() + 1 );
    intervalos7.push( toString(d13) );
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
    
    //agosto
   
    let d15 = toDate("01/08/2022"),
    d16 = toDate("31/08/2022"),
    intervalos8 = [];

    intervalos8.push( toString(d15) );

    while ( d15 < d16 ) {
    d15.setDate( d15.getDate() + 1 );
    intervalos8.push( toString(d15) );
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
    
    //setembro
    
    let d17 = toDate("01/09/2022"),
    d18 = toDate("30/09/2022"),
    intervalos9 = [];

    intervalos9.push( toString(d17) );

    while ( d17 < d18 ) {
    d17.setDate( d17.getDate() + 1 );
    intervalos9.push( toString(d17) );
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

    
    //outubro
    
    let d19 = toDate("01/10/2022"),
    d20 = toDate("31/10/2022"),
    intervalos10 = [];

    intervalos10.push( toString(d19) );

    while ( d19 < d20 ) {
    d19.setDate( d19.getDate() + 1 );
    intervalos10.push( toString(d19) );
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

    
    //novembro
    
    let d21 = toDate("01/11/2022"),
    d22 = toDate("30/11/2022"),
    intervalos11 = [];

    intervalos11.push( toString(d21) );

    while ( d21 < d22 ) {
    d21.setDate( d21.getDate() + 1 );
    intervalos11.push( toString(d21) );
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

    
    //dezembro
    
    let d23 = toDate("01/12/2022"),
    d24 = toDate("31/12/2022"),
    intervalos12 = [];

    intervalos12.push( toString(d23) );

    while ( d23 < d24 ) {
    d23.setDate( d23.getDate() + 1 );
    intervalos12.push( toString(d23) );
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
    

    
   