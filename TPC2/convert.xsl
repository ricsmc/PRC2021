<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="2.0">
    
    <xsl:output method="text" encoding="UTF-8" indent="yes"/>
    
    <xsl:template match="obra">
        <xsl:text>

        </xsl:text>
        ### http://www.di.uminho.pt/prc2021/tpc2#o_<xsl:value-of select="@id"/>
        :o_<xsl:value-of select="@id"/> rdf:type owl:NamedIndividual ,
        :Obra ;
        <xsl:if test="inf-relacionada">
            :video "<xsl:value-of select="inf-relacionada/video/@href"/>" ;
        </xsl:if> 
        <xsl:if test="titulo">
            :titulo "<xsl:value-of select="titulo"/>" ;
        </xsl:if>

        <xsl:if test="compositor">
            :compositor "<xsl:value-of select="compositor"/>" ;
        </xsl:if> 
        <xsl:if test="subtitulo">
            :subtitulo "<xsl:value-of select="subtitulo"/>" ;
        </xsl:if> 
        <xsl:if test="arranjo">
            :arranjo "<xsl:value-of select="arranjo"/>" ;
        </xsl:if> 
        <xsl:if test="editado">
            :editado "<xsl:value-of select="editado"/>" ;
        </xsl:if> 
        <xsl:if test="tipo">
            :tipo "<xsl:value-of select="tipo"/>" .
        </xsl:if> 
        
        <xsl:if test="compositor">
            ### http://www.di.uminho.pt/prc2021/tpc2#<xsl:value-of select="replace(replace(replace(normalize-unicode(compositor, 'NFKD'), '\P{IsBasicLatin}', ''),' ','_'),',','')"/>
            :<xsl:value-of select="replace(replace(replace(normalize-unicode(compositor, 'NFKD'), '\P{IsBasicLatin}', ''),' ','_'),',','')"/> rdf:type owl:NamedIndividual ,
            :Compositor ;
            :compos :o_<xsl:value-of select="@id"/> ;
            :nome "<xsl:value-of select="replace(replace(replace(normalize-unicode(compositor, 'NFKD'), '\P{IsBasicLatin}', ''),' ','_'),',','')"/>" .
        </xsl:if>
        
        <xsl:for-each select="instrumentos/instrumento">
            ### http://www.di.uminho.pt/prc2021/tpc2#<xsl:value-of select="replace(replace(replace(normalize-unicode(designacao, 'NFKD'), '\P{IsBasicLatin}', ''),' ','_'),',','')"/>
            :<xsl:value-of select="replace(replace(replace(normalize-unicode(designacao, 'NFKD'), '\P{IsBasicLatin}', ''),' ','_'),',','')"/> rdf:type owl:NamedIndividual,
            :Instrumento ;
            :utilizadoEm :o_<xsl:value-of select="../../@id"/> ;
            :designação "<xsl:value-of select="replace(replace(replace(normalize-unicode(designacao, 'NFKD'), '\P{IsBasicLatin}', ''),' ','_'),',','')"/>" .
            
            <xsl:for-each select="partitura">
                ### http://www.di.uminho.pt/prc2021/tpc2#partitura_<xsl:value-of select="@path"/>
                :<xsl:value-of select="@path"/> rdf:type owl:NamedIndividual ,
                :Partitura ;
                :pertenceA :instrumento_<xsl:value-of select="replace(replace(replace(normalize-unicode(designacao, 'NFKD'), '\P{IsBasicLatin}', ''),' ','_'),',','')"/> ;
                :path "<xsl:value-of select="@path"/>" ;
                <xsl:if test="@afinacao">:afinacao "<xsl:value-of select="@afinacao"/>" ; </xsl:if>          
                <xsl:if test="@clave">:clave "<xsl:value-of select="@clave"/>" ; </xsl:if>
                <xsl:if test="@voz">:voz "<xsl:value-of select="@voz"/>" ; </xsl:if> 
                :type "<xsl:value-of select="@type"/>" .
            </xsl:for-each>
            
        </xsl:for-each>
    </xsl:template>
</xsl:stylesheet>