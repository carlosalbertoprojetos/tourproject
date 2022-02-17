window.addEventListener('DOMContentLoaded', event => {
    // Simple-DataTables
    // https://github.com/fiduswriter/Simple-DataTables/wiki

    const datatablesSimple = document.getElementById('datatablesSimple');
    if (datatablesSimple) {
        new simpleDatatables.DataTable(
            datatablesSimple, {
        });
    }
});

// $('#datatablesSimple').DataTable({
//     "language": {
//         "sProcessing":    "Procesando...",
//         "sLengthMenu":    "Exibir _MENU_ registros por página",
//         "sZeroRecords":   "Nenhum resultado encontrado",
//         "sEmptyTable":    "Nenhum resultado encontrado",
//         "sInfo":          "Exibindo do _START_ até _END_ de um total de _TOTAL_ registros",
//         "sInfoEmpty":     "Exibindo do 0 até 0 de um total de 0 registros",
//         "sInfoFiltered":  "(Filtrado de um total de _MAX_ registros)",
//         "sInfoPostFix":   "",
//         "sSearch":        "Buscar:",
//         "sUrl":           "",
//         "sInfoThousands":  ",",
//         "sLoadingRecords": "Cargando...",
//         "oPaginate": {
//             "sFirst":    "Primero",
//             "sLast":    "Último",
//             "sNext":    "Próximo",
//             "sPrevious": "Anterior"
//         },
//         "oAria": {
//             "sSortAscending":  ": Ativar para ordenar a columna de maneira ascendente",
//             "sSortDescending": ": Ativar para ordenar a columna de maneira descendente"
//         }
//     }
// });


// $(document).ready(function() {
//     $('#datatablesSimple').dataTable( {
//             "oLanguage": {
//                 "sLengthMenu": "Display _MENU_ records per page",
//                 "sZeroRecords": "Nothing found - sorry",
//                 "sInfo": "Showing _START_ to _END_ of _TOTAL_ records",
//                 "sInfoEmpty": "Showing 0 to 0 of 0 records",
//                 "sInfoFiltered": "(filtered from _MAX_ total records)"
//             }
//         } );
//     } );


// let dataTable = new DataTable("#datatablesSimple" {
//     "language": {
//         "url": "https://cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Portuguese-Brasil.json"
//     },
// });

