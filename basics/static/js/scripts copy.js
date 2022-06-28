/*!
* Start Bootstrap - Bare v5.0.7 (https://startbootstrap.com/template/bare)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-bare/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

/*!
    * Start Bootstrap - SB Admin v7.0.4 (https://startbootstrap.com/template/sb-admin)
    * Copyright 2013-2021 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-sb-admin/blob/master/LICENSE)
    */
// 
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

});


    // $(function campos() {
    //     $("#id_num_child").keyup(() => {
    //         let num_child = $("#id_num_child").val();
    //         const campos = $("#id_child_package_one_set-0"); // id_child_package_one_set-0
    //         const message = $("#message");
    //         message.empty()

    //         if (num_child) {
    //             num_child = parseInt(num_child);

    //             message.append('Por favor, informe a idade das crianças')
    //             campos.empty();

    //             i=1
    //             while (i <= num_child) {
    //                 texto = 'child_package_one_set-0'
    //                 texto.replace(/-0/g, '-' + i.toString())
    //                 i = i + 1;
    //             }

    //             $('#span-real').html(texto)

    //         }
    //     });
    // });

    // function Somar() {
    //     const inputs = $(".soma");
    //     let total = 0;
    //     }

    $(function camposParcela() {
        // 'spantestemodelo' recebe todas as informações contidas no id="span-modelo"
        var spantestemodelo = $('#span-modelo').html();
        // transforma todos os dados de 'spamtestemodelo' em string
        var spantestemodelo_string = spantestemodelo.toString();
        // campos recebe o valor contido no id="numero-parcelas"
        var campos = $('#id_num_child').val();

        // individualizar id dinamicamente
        var i;
        i=1;
        var texto = '';
        while (i <= campos) {
            texto = texto + spantestemodelo_string.replace(/-0/g, '-' + i.toString())
            //converte o inteiro 'i' para string - /-0/g para que seja feita em todos que possuem -0 de forma 'g' globalmente
            console.log(i)
            i = i + 1;
        }

        // converte tudo que estiver em 'texto' conforme as configurações no id="span-real"
        $('#span-real').html(texto);
    });

