# Kick off django config machinery first

from Orm.db.models import *
#from django.conf import settings
#settings.configure(TEMPLATE_DIRS=("",))

import django.template
import django.template.loader


def render(name, *values):
    ctx = django.template.Context()
    for d in values:
        ctx.push()
        ctx.update(d)

    t = django.template.loader.get_template(name)
    return t.render(ctx)


kunde = Kunde.objects.all()[0]

r = render('test.html', dict({'kunde': kunde}))

print r

f = open('rendered.html', 'w')
f.write(r.encode('utf-8'))
f.close()
