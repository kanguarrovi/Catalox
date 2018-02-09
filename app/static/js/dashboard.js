function delete_file(album_id){
  swal({
    title: "Delete album",
    text: "Once deleted, you will not be able to recover this album information!",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  }).then((willDelete) => {
      if (willDelete) {
        $.ajax({
          type: "POST",
          url: '/delete_album/' + album_id,
        });
        swal("Poof! The album has been deleted!", {
          icon: "success",
        });
        /*This line must be deleted*/
        window.location.reload();
      } else {
        swal("The album has not been deleted!");
      }
  });
}