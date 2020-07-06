.. image:: https://img.shields.io/badge/license-AGPL--3-blue.png
   :target: https://www.gnu.org/licenses/agpl
   :alt: License: AGPL-3

=========================================
Modulo Base para los Web Services de AFIP
=========================================

Homologation / Production:
--------------------------

Primero busca un parámetro "afip.ws.env.type" si existe y:

* Es Producción --> production
* Es Homologación --> homologation

Ademas

Busque el parámetro 'server_mode' en el archivo conf. Si ese parámetro:

* Tiene un valor, entonces usamos "homologación".
* Si no hay parámetro, entonces "producción".

Incluye:
--------

* Wizard para instalar los claves para acceder a las Web Services.
* API para realizar consultas en la Web Services desde OpenERP.

El módulo l10n_ar_afipws permite a OpenERP acceder a los servicios del AFIP a
travésde Web Services. Este módulo es un servicio para administradores y
programadores, donde podrían configurar el servidor, la autentificación
y además tendrán acceso a una API genérica en Python para utilizar los
servicios AFIP.

Tenga en cuenta que estas claves son personales y pueden traer conflicto
publicarlas en los repositorios públicos.
