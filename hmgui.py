"""
A program that lets me store data about Horror Movies I've watched (Film name, director, FX artist, year released, 1-5 rating and date watched)
Uses Postgres for the back-end.

User can: 
View records
Search records
Create/Delete records
Close application
"""

''' TODO: Current bug/unintended behavior when deleting records - it should be using the entryID as the identifier, however, it deletes all that have the movie name '''

from tkinter import *
from sql import Backend
bk = Backend()
window = Tk()
window.title("Horror Movie Record")

class Btn_Commands():
    '''This class creates an object to use in calling the button commands'''

    def __init__(self):
        self=self


    def intermediate_view(self):
        result_box.delete(0, END)
        result = bk.view()
        for x in result:
            result_box.insert(END, x)

    def intermediate_search(self):
        result_box.delete(0, END)
        result = bk.search(main_movie_name_entry.get(),
        main_director_entry.get(), 
        main_fxartist_entry.get(), 
        main_year_entry.get(), 
        main_rating_entry.get(), 
        main_date_entry.get())
        for x in result:
            result_box.insert(END, x)

    def intermediate_delete(self):
        bk.delete(result_box.get(ACTIVE)[0])
        result_box.delete(0, END)
        for x in bk.view():
            result_box.insert(END, x)
        

    def intermediate_add(self):
        bk.insert(main_movie_name_entry.get(), main_director_entry.get(), 
        main_fxartist_entry.get(),
        main_year_entry.get(), main_rating_entry.get(), 
        main_date_entry.get())
        result_box.insert(END, (main_movie_name_entry.get(), main_director_entry.get(), 
        main_fxartist_entry.get(),
        main_year_entry.get(), main_rating_entry.get(), 
        main_date_entry.get()))

    def intermediate_update(self):
        bk.update(main_movie_name_entry.get(), main_director_entry.get(), 
        main_fxartist_entry.get(),
        main_year_entry.get(), main_rating_entry.get(), 
        main_date_entry.get(), result_box.get(ACTIVE)[6])
        result_box.delete(0, END)
        for x in bk.view():
            result_box.insert(END, x)

def entry_bind(evt):
    main_movie_name_entry.delete(0, END)
    main_director_entry.delete(0, END)
    main_fxartist_entry.delete(0, END)
    main_year_entry.delete(0, END)
    main_rating_entry.delete(0, END)
    main_date_entry.delete(0, END)
    w = evt.widget
    value = w.get(w.curselection())
    main_movie_name_entry.insert(0, value[0])
    main_director_entry.insert(0, value[1])
    main_fxartist_entry.insert(0, value[2])
    main_year_entry.insert(0, value[3])
    main_rating_entry.insert(0, value[4])
    main_date_entry.insert(0, value[5])

commands = Btn_Commands()
    
main_movie_name_entry = Entry(window)
main_movie_name_entry.grid(row=0, column=1)
main_director_entry = Entry(window)
main_director_entry.grid(row=0, column=3)
main_fxartist_entry = Entry(window)
main_fxartist_entry.grid(row=1, column=1)
main_year_entry = Entry(window)
main_year_entry.grid(row=1, column=3)
main_rating_entry = Entry(window)
main_rating_entry.grid(row=2, column=1)
main_date_entry = Entry(window)
main_date_entry.grid(row=2, column=3)
main_movie_name_lbl = Label(window, text="Movie Name:")
main_movie_name_lbl.grid(row=0, column=0)
main_director_lbl = Label(window, text="Director:")
main_director_lbl.grid(row=0, column=2)
main_fxartist_lbl = Label(window, text="FX Artist:")
main_fxartist_lbl.grid(row=1, column=0)
main_year_lbl = Label(window, text="Year:")
main_year_lbl.grid(row=1, column=2)
main_rating_lbl = Label(window, text="Rating:")
main_rating_lbl.grid(row=2, column=0)
main_date_lbl = Label(window, text="Date Watched:")
main_date_lbl.grid(row=2, column=2)
view_btn = Button(window, text="View all", command=commands.intermediate_view)
view_btn.grid(row=3, column=6)
search_btn = Button(window, text="Search entry", command=commands.intermediate_search)
search_btn.grid(row=4, column=6)
delete_btn = Button(window, text="Delete entry", command=commands.intermediate_delete)
delete_btn.grid(row=5, column=6)
add_btn = Button(window, text="Add entry", command=commands.intermediate_add)
add_btn.grid(row=6, column=6)
update_btn = Button(window, text="Update", command=commands.intermediate_update)
update_btn.grid(row=7, column=6)
close_btn = Button(window, text="Close", command=window.destroy)
close_btn.grid(row=8, column=6)
result_box = Listbox(window, height=6, width=55)
result_box.grid(row=4, column=0, rowspan=6, columnspan=2)
sb1=Scrollbar(window)
sb1.grid(row=4, column=3, rowspan=6)
result_box.configure(yscrollcommand=sb1.set)
sb1.configure(command=result_box.yview)
selection = result_box.bind('<<ListboxSelect>>', entry_bind)







window.mainloop()


