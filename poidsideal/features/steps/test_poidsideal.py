# -*- coding: utf-8 -*-
"""
SVL 2015-2016
TP poids ideal
Authors: Honore Nintunze, Antonin Durey
"""

# Fonctionnalités
# - calculer poids idéal
# *on rentre un nombre dans un input et le resultat s'affiche


import behave
from selenium import webdriver
import nose.tools
from poidsideal import *


class TestPageCalculPoidsIdeal:

    # setup fonction without behave
    # @classmethod
    # def setUpClass(cls):
    #     cls.navigateur = webdriver.Firefox()
    #     cls.navigateur.get('http://localhost:8080')
    #
    # @classmethod
    # def tearDownClass(cls):
    #     cls.navigateur.quit()

    @when('I am on the convertor page')
    def step_impl(context):
        pass

    @then('The right title is displayed')
    def step_impl(context):
        titre = context.navigateur.title

        nose.tools.assert_equal(titre, 'Calcul poids idéal')

    # without behave
    # def test_la_page_a_un_titre(self):
    #     titre = self.navigateur.title
    #
    #     nose.tools.assert_equal(titre, 'Calcul poids idéal')

    @then('The page contains an input field')
    def step_impl(context):
        boite = context.navigateur.find_element_by_id('taille')
        letype = boite.get_attribute('type')

        nose.tools.assert_equal('number', letype)

    # without behave
    # def test_la_page_contient_ne_boite_de_saisie(self):
    #     boite = self.navigateur.find_element_by_id('taille')
    #     letype = boite.get_attribute('type')
    #
    #     nose.tools.assert_equal('number', letype)

class TestCalculPoidsIdeal:

    # setup fonction without behave
    # @classmethod
    # def setUpClass(cls):
    #     cls.navigateur = webdriver.Firefox()
    #     cls.navigateur.get('http://localhost:8080')
    #
    # @classmethod
    # def tearDownClass(cls):
    #     cls.navigateur.quit()

    @given('I am on the convertor page')
    def step_impl(context):
        pass

    @when('I enter a non positive value')
    def step_impl(context):
        boite = context.navigateur.find_element_by_id('taille')
        boite.send_keys("-2")
        boite.submit()

    @then('I can see an error message')
    def step_impl(context):
        message_erreur = context.navigateur.find_element_by_id('mess_err').text
        nose.tools.assert_equal(message_erreur, 'Le poids doit être positif')

    # without behave
    # def test_la_valeur_entree_est_negative(self):
    #     boite = self.navigateur.find_element_by_id('taille')
    #     boite.send_keys("-2\n")
    #
    #     message_erreur = self.navigateur.find_element_by_id('mess_err')
    #
    #     nose.tools.assert_equal(message_erreur.text, 'Le poids doit être positif')
    #

    @given('I am on the convertor page as a man')
    def step_impl(context):
        pass

    @when('I enter a height value, and the man checkbox is checked and then validate')
    def step_impl(context):
        radio = context.navigateur.find_element_by_id('homme')
        radio.click()
        boite = context.navigateur.find_element_by_id('taille')
        boite.send_keys("180")
        boite.submit()

    @then('I can see the corresponding weight for a man')
    def step_impl(context):
        message_erreur = context.navigateur.find_element_by_id('mess_result')

        nose.tools.assert_equal(message_erreur.text, 'Votre poids idéal est : 73 kg')

    # without behave
    # def test_la_valeur_entree_est_positive_on_a_le_bon_resultat_homme(self):
    #     radio = self.navigateur.find_element_by_id('homme')
    #     radio.click()
    #     boite = self.navigateur.find_element_by_id('taille')
    #     boite.send_keys("180\n")
    #
    #     message_erreur = self.navigateur.find_element_by_id('mess_result')
    #
    #     nose.tools.assert_equal(message_erreur.text, 'Votre poids idéal est : 73 kg')

    @given('I am on the convertor page as a woman')
    def step_impl(context):
        pass

    @when('I enter a height value, and the woman checkbox is checked and then validate')
    def step_impl(context):
        radio = context.navigateur.find_element_by_id('femme')
        radio.click()
        boite = context.navigateur.find_element_by_id('taille')
        boite.send_keys("160")
        boite.submit()

    @then('I can see the corresponding weight for a woman')
    def step_impl(context):
        message_erreur = context.navigateur.find_element_by_id('mess_result')

        nose.tools.assert_equal(message_erreur.text, 'Votre poids idéal est : 56.0 kg')

    # without behave
    # def test_la_valeur_entree_est_positive_on_a_le_bon_resultat_femme(self):
    #     radio = self.navigateur.find_element_by_id('femme')
    #     radio.click()
    #     boite = self.navigateur.find_element_by_id('taille')
    #     boite.send_keys("160\n")
    #
    #     message_erreur = self.navigateur.find_element_by_id('mess_result')
    #
    #     nose.tools.assert_equal(message_erreur.text, 'Votre poids idéal est : 56.0 kg')

# without behave
# class TestCalculateurPoidsIdeal:
#
#     def test_taille_negatif_donc_erreur(self):
#         calculateur = Calculateur()
#         nose.tools.assert_raises(ValueError, calculateur.calcule, -180, 'h')
#
#     def test_taille_positif_et_femme(self):
#         calculateur = Calculateur()
#         nose.tools.assert_equal(calculateur.calcule(160, 'f'), 56.0)
#
#     def test_taille_positif_et_homme(self):
#         calculateur = Calculateur()
#         nose.tools.assert_equal(calculateur.calcule(180, 'h'), 72.5)
