# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from odoo import api, models, fields


class Biblioteca(models.Model):

    _name = b'library'

    name = fields.Char(
        string='Nome',
    )

    diretor = fields.Many2one(
        comodel_name='res.users',
        string='Diretor Autoritario',
        required=True,
    )

    state = fields.Selection([
        ('novo', 'Novo'),
        ('confirmado', 'Confirmado'),
        ('enviado', 'Enviado'),
        ('publicado', 'Publicado'),
        ('cancelado', 'cancelado')],
        string='State',
        default='novo',
    )

    livros_ids = fields.Many2many(
        comodel_name='library.book',
        inverse_name='biblioteca_id',
        string='Livros',
        domain="[('state', '=', state)]"
    )

    names = fields.Char(
        string='Nomes da galera',
    )

    @api.onchange('livros_id')
    def onchange_livros_id(self):
        names = ''
        for record in self:
            for livro in record.livros_ids:
                names += livro.name
            record.names = names
