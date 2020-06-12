 # -*- coding: utf-8 -*-
from openfisca_france.model.base import Variable, Individu, MONTH

from numpy import (
    maximum as max_,
    minimum as min_,
    round as round_,
)


class salaire_journalier_reference(Variable):
    entity = Individu
    value_type = float
    definition_period = MONTH


class temps_travail_semaine(Variable):
    entity = Individu
    value_type = float
    definition_period = MONTH


class agepi(Variable):
    entity = Individu
    value_type = float
    definition_period = MONTH
    default_value = 12


class complement_are_jours_base(Variable):
    entity = Individu
    value_type = float
    definition_period = MONTH

    def formula(individu, period):
        are_j = individu('are_j', period)
        are_m = are_j * 30

        salaire = individu('salaire_de_base', period)
        return (are_m - 0.7 * salaire) / are_j


class complement_are_jours(Variable):
    entity = Individu
    value_type = float
    definition_period = MONTH

    def formula(individu, period):
        are_j = individu('are_j', period)
        nb_jours = individu('complement_are_jours_base', period)

        salaire = individu('salaire_de_base', period)
        plafond_e = individu('salaire_journalier_reference', period) * 30.42

        return round_((min_(plafond_e, are_j * nb_jours + salaire) - salaire) / are_j)


class complement_are(Variable):
    entity = Individu
    value_type = float
    definition_period = MONTH

    def formula(individu, period):
        salaire = individu('salaire_de_base', period)
        are_j = individu('are_j', period)
        nb_jours = individu('complement_are_jours', period)

        return are_j * nb_jours * (salaire > 0)


class are_j(Variable):
    entity = Individu
    value_type = float
    definition_period = MONTH
    
    def formula(individu, period):
        sjr = individu('salaire_journalier_reference', period)
        base_pct = (12 + 0.404 * sjr) / sjr
        return min_(0.75, max_(0.57, base_pct)) * sjr
