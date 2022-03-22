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
    if(window.confirm("Wollen Sie diesne Lehrer wirklich löschen"))
    {
        button.form.submit(this);
    }
}