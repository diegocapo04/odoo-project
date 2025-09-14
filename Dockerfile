FROM odoo:17.0

COPY ./addons mnt/extra-addons 

CMD ["odoo", "--addons-path=/mnt/extra-addons,/usr/lib/python3/dist-packages/odoo/addons"]