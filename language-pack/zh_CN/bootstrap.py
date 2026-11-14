# -*- coding: utf-8 -*-
"""External zh-CN language pack bootstrap for FEFW Save Editor."""
from __future__ import annotations

_INSTALLED = False

def install():
    global _INSTALLED
    if _INSTALLED:
        return
    import i18n_zh_cn
    import zh_cn_names
    import fefw_save
    import fefw_layer

    # Install UI text translation before the editor creates its widgets.
    i18n_zh_cn.install()

    # Catalogue names are presentation-only; IDs and save bytes remain untouched.
    _old_item_label = fefw_save.item_label
    def _item_label(iid, meta=None):
        meta = fefw_save.item_ids().get(iid) if meta is None else meta
        return zh_cn_names.item_name(meta) if meta else _old_item_label(iid, meta)
    fefw_save.item_label = _item_label
    fefw_layer.item_label = _item_label

    _old_meta = fefw_layer._meta
    def _meta(person):
        meta = _old_meta(person)
        meta = dict(meta)
        meta["name"] = zh_cn_names.unit_name(meta)
        return meta
    fefw_layer._meta = _meta

    _old_job_name = fefw_save.job_name
    def _job_name(value):
        meta = fefw_save.job_ids().get(value)
        return zh_cn_names.class_name(meta) if meta else _old_job_name(value)
    fefw_save.job_name = _job_name
    fefw_layer.job_name = _job_name

    _old_skill_label = fefw_layer.skill_label
    def _skill_label(sid):
        meta = fefw_save.item_ids().get(sid & 0xFFFFFFFF)
        if meta:
            return zh_cn_names.skill_name(meta)
        skills = fefw_layer._skills()
        meta = skills.get(sid & 0xFFFFFFFF)
        return zh_cn_names.skill_name(meta) if meta else _old_skill_label(sid)
    fefw_layer.skill_label = _skill_label

    _INSTALLED = True
