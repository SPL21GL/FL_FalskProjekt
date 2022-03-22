function deleteSchul(button)
{
    console.log(button)
    if(window.confirm("Wollen Sie die Schule wirklich löschen"))
    {
        button.form.submit(this);
    }
}