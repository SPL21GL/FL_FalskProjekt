function deleteSchul(button)
{
    console.log(button)
    if(window.confirm("Wollen Sie die Schule wirklich löschen"))
    {
        button.form.submit(this);
    }
}

function deleteLehrer(button)
{
    console.log(button)
    if(window.confirm("Wollen Sie diesen Lehrer wirklich löschen"))
    {
        button.form.submit(this);
    }
}

function deleteFach(button)
{
    console.log(button)
    if(window.confirm("Wollen Sie dieses Fach wirklich löschen"))
    {
        button.form.submit(this);
    }
}