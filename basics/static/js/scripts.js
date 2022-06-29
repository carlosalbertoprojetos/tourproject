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

            message = document.getElementById('id_message')
            message.setAttribute('style', 'display:none;')
            
            if (quantidade) {
                quantidade = parseInt(quantidade);                
                
                for (let i=0; i < quantidade; i++) {                    
                    message = document.getElementById('id_message')
                    message.setAttribute('style', 'display:flex;')

                    const currentChildAgeForms = document.getElementsByClassName('child_age_form')
                    const currentFormCount = currentChildAgeForms.length

                    const formCopyTarget = document.getElementById('children_age_list')
                    const copyEmptyFormEl = document.getElementById('empty-form').cloneNode(true)
                    copyEmptyFormEl.setAttribute('class', 'child_age_form')
                    copyEmptyFormEl.setAttribute('id', `id_child_package_one_set-${currentFormCount}-children_age`)
                    const regex =  new RegExp('__prefix__', 'g')
                    copyEmptyFormEl.innerHTML = copyEmptyFormEl.innerHTML.replace(regex, currentFormCount)
                    totalNewForms.setAttribute('value', currentFormCount + 1)
                    formCopyTarget.append(copyEmptyFormEl)
                }
            }
        })
    });