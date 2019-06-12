﻿# -*- coding: utf-8 -*-


def reset():
    from . import models
    
    tables = [
        models.Department, models.Role,
        models.Project, models.Edition, models.Genus, models.Tag,
        models.Entity, models.Stage, models.Status, models.Task
    ]
    
    for table in tables:
        for data in table.objects.all():
            data.delete()

    # Department
    for data in [
        {'name': u'global',    'info': u'统筹'},
        {'name': u'design',    'info': u'原画'},
        {'name': u'modeling',  'info': u'模型'},
        {'name': u'rigging',   'info': u'绑定'},
        {'name': u'animation', 'info': u'动画'},
        {'name': u'rendering', 'info': u'渲染'},
    ]: models.Department(**data).save()

    # Role
    for data in [
        {'name':'staff', 'info':u'制作人员'},
        {'name':'supervisor', 'info':u'组长'},
        {'name':'producer', 'info':u'制片'},
        {'name':'director', 'info':u'导演'},
        {'name':'administrator', 'info':u'管理员'},
    ]: models.Role(**data).save()
    
    # Project
    for data in [
        {'name': u'TEMPLATE', 'info': u'模板项目', 'root': u'P:/'},
    ]: models.Project(**data).save()
    
    # Genus
    for data in [
        {'name':'asset', 'info':u'资产'},
        {'name':'shot',  'info':u'镜头'},
        {'name':'batch', 'info':u'批次'},
    ]: models.Genus(**data).save()
    
    # Tag
    prj = models.Project.objects.get(name='TEMPLATE')
    gns_batch = models.Genus.objects.get(name='batch')
    gns_asset = models.Genus.objects.get(name='asset')
    for data in [
        {'project': prj, 'genus': gns_batch, 'name': u'episode', 'info': u'集数'},
        {'project': prj, 'genus': gns_batch, 'name': u'scene', 'info': u'场次'},
        {'project': prj, 'genus': gns_asset, 'name': u'CH', 'info': u'角色'},
        {'project': prj, 'genus': gns_asset, 'name': u'PR', 'info': u'道具'},
        {'project': prj, 'genus': gns_asset, 'name': u'SC', 'info': u'场景'},
    ]: models.Tag(**data).save()
    
    # Stage
    gns_shot = models.Genus.objects.get(name='shot')
    for data in [
        {'project':prj, 'genus':gns_batch, 'name':u'scp', 'info':u'剧本', 'source':u'{project}/{stage}/{entity}/',                           'data':u'{project}/UE/'},
        {'project':prj, 'genus':gns_batch, 'name':u'stb', 'info':u'分镜', 'source':u'{project}/{stage}/{entity}/',                           'data':u'{project}/UE/'},
        {'project':prj, 'genus':gns_batch, 'name':u'dub', 'info':u'配音', 'source':u'{project}/{stage}/{entity}/',                           'data':u'{project}/UE/'},
        {'project':prj, 'genus':gns_asset, 'name':u'dsn', 'info':u'原画', 'source':u'{project}/{genus}/{tag}/{entity}/{stage}/',             'data':u'{project}/UE/{genus}/{tag}/{entity}/'},
        {'project':prj, 'genus':gns_asset, 'name':u'mdl', 'info':u'建模', 'source':u'{project}/{genus}/{tag}/{entity}/{entity}_{stage}.ma',  'data':u'{project}/UE/{genus}/{tag}/{entity}/'},
        {'project':prj, 'genus':gns_asset, 'name':u'txt', 'info':u'贴图', 'source':u'{project}/{genus}/{tag}/{entity}/{stage}/',             'data':u'{project}/UE/{genus}/{tag}/{entity}/'},
        {'project':prj, 'genus':gns_asset, 'name':u'shd', 'info':u'材质', 'source':u'{project}/{genus}/{tag}/{entity}/{stage}/',             'data':u'{project}/UE/{genus}/{tag}/{entity}/'},
        {'project':prj, 'genus':gns_asset, 'name':u'skn', 'info':u'蒙皮', 'source':u'{project}/{genus}/{tag}/{entity}/{entity}_{stage}.ma',  'data':u'{project}/UE/{genus}/{tag}/{entity}/'},
        {'project':prj, 'genus':gns_asset, 'name':u'rig', 'info':u'绑定', 'source':u'{project}/{genus}/{tag}/{entity}/{entity}_{stage}.ma',  'data':u'{project}/UE/{genus}/{tag}/{entity}/'},
        {'project':prj, 'genus':gns_asset, 'name':u'prv', 'info':u'预览', 'source':u'{project}/{genus}/{tag}/{entity}/{stage}/',             'data':u'{project}/UE/{genus}/{tag}/{entity}/'},
        {'project':prj, 'genus':gns_shot,  'name':u'lyt', 'info':u'布局', 'source':u'{project}/{genus}/{stage}/{project}_{tag}_{entity}.ma', 'data':u'{project}/UE/{genus}/{stage}/{entity}/'},
        {'project':prj, 'genus':gns_shot,  'name':u'anm', 'info':u'动画', 'source':u'{project}/{genus}/{stage}/{project}_{tag}_{entity}.ma', 'data':u'{project}/UE/{genus}/{stage}/{entity}/'},
        {'project':prj, 'genus':gns_shot,  'name':u'cfx', 'info':u'解算', 'source':u'{project}/{genus}/{stage}/{project}_{tag}_{entity}.ma', 'data':u'{project}/UE/{genus}/{stage}/{entity}/'},
        {'project':prj, 'genus':gns_shot,  'name':u'lgt', 'info':u'灯光', 'source':u'{project}/{genus}/{stage}/{project}_{tag}_{entity}/',   'data':u'{project}/UE/{genus}/{stage}/{entity}/'},
        {'project':prj, 'genus':gns_shot,  'name':u'rnd', 'info':u'渲染', 'source':u'{project}/{genus}/{stage}/{project}_{tag}_{entity}/',   'data':u'{project}/UE/{genus}/{stage}/{entity}/'},
        {'project':prj, 'genus':gns_shot,  'name':u'vfx', 'info':u'特效', 'source':u'{project}/{genus}/{stage}/{project}_{tag}_{entity}/',   'data':u'{project}/UE/{genus}/{stage}/{entity}/'},
        {'project':prj, 'genus':gns_shot,  'name':u'cmp', 'info':u'合成', 'source':u'{project}/{genus}/{stage}/{project}_{tag}_{entity}/',   'data':u'{project}/UE/{genus}/{stage}/{entity}/'},
    ]: models.Stage(**data).save()

    # Entity
    tag_eps = models.Tag.objects.get(name='episode', project=prj)
    tag_ch  = models.Tag.objects.get(name='CH', project=prj)
    for data in [
        {'tag':tag_eps, 'name':u'EP01',  'info':u'第一集'},
        {'tag':tag_ch,  'name':u'Danny', 'info':u'丹尼'},
    ]: models.Entity(**data).save()
    tag_ep01 = models.Tag.objects.get(name='EP01', project=prj)
    models.Entity(tag=tag_ep01, name='SC001', info=u'SC001').save()
    
    # Status
    for data in [
        {'name':u'initialized', 'info':u'初始化'},
        {'name':u'assigned',    'info':u'已分配'},
        {'name':u'submitted',   'info':u'已提交'},
        {'name':u'approved',    'info':u'已通过'},
        {'name':u'unapproved',  'info':u'未通过'},
        {'name':u'expired',     'info':u'已过期'},
        {'name':u'ignored',     'info':u'已忽略'},
    ]: models.Status(**data).save()
    
    #Task
    ent = models.Entity.objects.get(name='Danny')
    sta = models.Status.objects.get(name='initialized')
    stg_mdl = models.Stage.objects.get(name='mdl')
    stg_skn = models.Stage.objects.get(name='skn')
    for data in [
        {'entity': ent, 'stage': stg_mdl, 'status': sta},
        {'entity': ent, 'stage': stg_skn, 'status': sta},
    ]: models.Task(**data).save()


if __name__ == "__main__":
    reset()
