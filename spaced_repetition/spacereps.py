import os

import fire
from tinydb import TinyDB, Query

from utils import print_header, print_resource, string_to_date, date_to_string
from card import Card

DB = TinyDB(os.path.join(os.path.expanduser('~'), 'resources.json'))

class SpacedRepetitor(object):
  """A simple spaced repetition class."""

  def add(self, url, name, grade = 5):
    c = Card()
    c.update(grade)
    DB.insert({ 'url': url, 'name': name, 'due_time': date_to_string(c.due_time), 'repetitions': c.repetitions, 'interval': c.interval })

  def update(self, id, grade):
    resource = DB.get(doc_id = id)
    c = Card(resource['repetitions'], interval=resource['interval'])
    c.update(grade)
    resource.update({ 'due_time': date_to_string(c.due_time), 'repetitions': c.repetitions, 'interval': c.interval })
    DB.update(resource, doc_ids=[resource.doc_id])

  def remove(self, id):
    DB.remove(doc_ids = [id])

  def all(self):
    resources = DB.all()
    print(f'Resources total: {len(resources)}\n')
    if not len(resources): return
    print_header()
    for r in resources:
      print_resource(r)
    print('\n')

  def due(self):
    resources = DB.all()
    due = []
    for r in resources:
      c = Card(r['repetitions'], r['interval'], due_time=string_to_date(r['due_time']))
      if c.is_due():
        due.append(r)
    print(f'Resources due: {len(due)}\n')
    if not len(due): return
    print_header()


if __name__ == '__main__':
  fire.Fire(SpacedRepetitor)
