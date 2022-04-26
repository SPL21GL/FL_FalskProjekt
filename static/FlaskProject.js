function deleteSchul(button)
{
    if(window.confirm("Wollen Sie die Schule wirklich löschen"))
    {
        button.form.submit(this);
    }
}

function deleteLehrer(button)
{
    if(window.confirm("Wollen Sie diesen Lehrer wirklich löschen"))
    {
        button.form.submit(this);
    }
}

function deleteFach(button)
{
    if(window.confirm("Wollen Sie dieses Fach wirklich löschen"))
    {
        button.form.submit(this);
    }
}