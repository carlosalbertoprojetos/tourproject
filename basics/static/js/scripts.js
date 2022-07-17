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


$(function () {
    $("#id_num_child").keyup(() => {
        var formCopyTarget = document.getElementById('children_age_list')
        while (formCopyTarget.firstChild) {
            formCopyTarget.removeChild(formCopyTarget.firstChild)
        }

        let quantidade = $("#id_num_child").val();
        const totalNewForms = document.getElementById('id_child_package_one_set-TOTAL_FORMS')

        if (quantidade) {
            quantidade = parseInt(quantidade);

            for (let i=0; i < quantidade; i++) {
                message = document.getElementById('id_message')
                message.setAttribute('style', 'display:flex;')

                const formCopyTarget = document.getElementById('children_age_list')
                const copyEmptyFormEl = document.getElementById('empty-form').cloneNode(true)
                copyEmptyFormEl.setAttribute('class', 'child_age_form')
                copyEmptyFormEl.setAttribute('id', `id_child_package_one_set-${i}-children_age`)
                const regex =  new RegExp('__prefix__', 'g')
                copyEmptyFormEl.innerHTML = copyEmptyFormEl.innerHTML.replace(regex, i)
                totalNewForms.setAttribute('value', i + 1)
                formCopyTarget.append(copyEmptyFormEl)
            }
        }
    });

    function null_or_empty(str) {
        var v = document.getElementById(str).value;
        return v == null || v == "";
    }
    
    $(function change_class() {

        let quantidade = $("#id_num_child").val();
        if (quantidade) {
            quantidade = parseInt(quantidade)

            for (let i=0; i < quantidade; i++) {
                if (null_or_empty(`id_child_package_one_set-${i}-children_age`))
                    alert('Por favor, informe as idade(s) da(s) criança(s)');
                    return false
                
                document.getElementById("profile-tab").removeAttribute("disabled");
                let a = document.querySelector('#profile');
                a.classList.add('show active');
                document.getElementById("accommodation-tab").removeAttribute("disabled");
                let b = document.querySelector('#accommodation');
                b.classList.add('show active');
                document.getElementById("transport-tab").removeAttribute("disabled");
                let c = document.querySelector('#transport');
                c.classList.add('show active');
                document.getElementById("data-tab").removeAttribute("disabled");
                let d = document.querySelector('#data');
                d.classList.add('show active');
            }
        }
    });
});