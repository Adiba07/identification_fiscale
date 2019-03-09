# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models


class Identification_fiscale(models.Model):
    _inherit = 'res.partner'
    nif = fields.Char(string="Numero identificatuon fiscal" ,size=15)
    nis = fields.Char(string="Numero identificatuon statique" ,size=15)
    numero_article = fields.Char(string="Numero d'article",size=11)
    numero_registre = fields.Char(string="Numero de registre")
    date_modification = fields.Date(string="dernie"
                                           "re modification")
    capitale_sociale = fields.Float(string="Capitale sociale")

    '''
    nif : numero identificatuon fiscal : taille =15 charaactere 
     = nis : numero identification statique .char taille 15 
     numero article : cahr condition 11 carachtere 
     numero_registre 
    la date de derniere modif type date :
    capitale sociale : float 
    '''