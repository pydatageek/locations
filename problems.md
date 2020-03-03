DRF is the source of web apis.

Django 2.2.10, DRF 3.11.0 and vue gets the latest from CDN.

Vuetify (again from CDN) gives material UI design with v-app-bar, v-navigation-drawer and v-footer.

Also Vuetify's v-data-table is used for two datasets. (countries and their cities)

I can show the data when the page first responded.

HOWEVER, when the drawer is closed with a button click or when the 'rows per page' of v-data-table has changed, data disappears. I should refresh the page to get it back.

error is:
Vue warn]: Avoid mutating a prop directly since the value will be overwritten whenever the parent component re-renders. Instead, use a data or computed property based on the prop's value. Prop being mutated: "tableData"

found in

---> <LocCountry>
<VContent>
<VApp>
<Root>
