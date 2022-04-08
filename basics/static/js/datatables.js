    $(document).ready( function () {
        $('#myTable1').DataTable({
            "language": {
              "url": "https://cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Portuguese-Brasil.json"
            },
            "lengthMenu" : [[5, 10, 25, 50, -1], [5, 10 ,25, 50, "Todos"]],
        });
    });