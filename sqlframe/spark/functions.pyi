from sqlframe.base.function_alternatives import (  # noqa
    percentile_without_disc as percentile,
    add_months_by_multiplication as add_months,
    arrays_overlap_renamed as arrays_overlap,
)
from sqlframe.base.functions import (
    abs as abs,
    acos as acos,
    acosh as acosh,
    aes_encrypt as aes_encrypt,
    aes_decrypt as aes_decrypt,
    aggregate as aggregate,
    approxCountDistinct as approxCountDistinct,
    approx_count_distinct as approx_count_distinct,
    array as array,
    array_contains as array_contains,
    array_distinct as array_distinct,
    array_except as array_except,
    array_intersect as array_intersect,
    array_join as array_join,
    array_max as array_max,
    array_min as array_min,
    array_position as array_position,
    array_remove as array_remove,
    array_repeat as array_repeat,
    array_sort as array_sort,
    array_union as array_union,
    arrays_zip as arrays_zip,
    asc as asc,
    asc_nulls_first as asc_nulls_first,
    asc_nulls_last as asc_nulls_last,
    ascii as ascii,
    asin as asin,
    asinh as asinh,
    assert_true as assert_true,
    atan as atan,
    atan2 as atan2,
    atanh as atanh,
    avg as avg,
    base64 as base64,
    bin as bin,
    bit_length as bit_length,
    bitwiseNOT as bitwiseNOT,
    bitwise_not as bitwise_not,
    bround as bround,
    cbrt as cbrt,
    ceil as ceil,
    ceiling as ceiling,
    coalesce as coalesce,
    col as col,
    collect_list as collect_list,
    collect_set as collect_set,
    concat as concat,
    concat_ws as concat_ws,
    conv as conv,
    corr as corr,
    cos as cos,
    cosh as cosh,
    cot as cot,
    count as count,
    countDistinct as countDistinct,
    count_distinct as count_distinct,
    covar_pop as covar_pop,
    covar_samp as covar_samp,
    crc32 as crc32,
    create_map as create_map,
    csc as csc,
    cume_dist as cume_dist,
    current_date as current_date,
    current_timestamp as current_timestamp,
    date_add as date_add,
    date_diff as date_diff,
    date_format as date_format,
    date_sub as date_sub,
    date_trunc as date_trunc,
    dayofmonth as dayofmonth,
    dayofweek as dayofweek,
    dayofyear as dayofyear,
    decode as decode,
    degrees as degrees,
    dense_rank as dense_rank,
    desc as desc,
    desc_nulls_first as desc_nulls_first,
    desc_nulls_last as desc_nulls_last,
    e as e,
    element_at as element_at,
    encode as encode,
    exists as exists,
    exp as exp,
    explode as explode,
    explode_outer as explode_outer,
    expm1 as expm1,
    expr as expr,
    factorial as factorial,
    filter as filter,
    first as first,
    flatten as flatten,
    floor as floor,
    forall as forall,
    format_number as format_number,
    format_string as format_string,
    from_csv as from_csv,
    from_json as from_json,
    from_unixtime as from_unixtime,
    from_utc_timestamp as from_utc_timestamp,
    get_json_object as get_json_object,
    greatest as greatest,
    grouping_id as grouping_id,
    hash as hash,
    hex as hex,
    hour as hour,
    hypot as hypot,
    initcap as initcap,
    input_file_name as input_file_name,
    instr as instr,
    isnan as isnan,
    isnull as isnull,
    json_tuple as json_tuple,
    kurtosis as kurtosis,
    lag as lag,
    last as last,
    last_day as last_day,
    lead as lead,
    least as least,
    length as length,
    levenshtein as levenshtein,
    lit as lit,
    locate as locate,
    log as log,
    log10 as log10,
    log1p as log1p,
    log2 as log2,
    lower as lower,
    lpad as lpad,
    ltrim as ltrim,
    make_date as make_date,
    make_interval as make_interval,
    map_concat as map_concat,
    map_entries as map_entries,
    map_filter as map_filter,
    map_from_arrays as map_from_arrays,
    map_from_entries as map_from_entries,
    map_keys as map_keys,
    map_values as map_values,
    map_zip_with as map_zip_with,
    max as max,
    max_by as max_by,
    md5 as md5,
    mean as mean,
    min as min,
    min_by as min_by,
    minute as minute,
    monotonically_increasing_id as monotonically_increasing_id,
    month as month,
    months_between as months_between,
    nanvl as nanvl,
    next_day as next_day,
    nth_value as nth_value,
    ntile as ntile,
    nullif as nullif,
    octet_length as octet_length,
    overlay as overlay,
    percent_rank as percent_rank,
    percentile_approx as percentile_approx,
    posexplode as posexplode,
    posexplode_outer as posexplode_outer,
    pow as pow,
    quarter as quarter,
    radians as radians,
    raise_error as raise_error,
    rand as rand,
    randn as randn,
    rank as rank,
    regexp_extract as regexp_extract,
    regexp_replace as regexp_replace,
    repeat as repeat,
    reverse as reverse,
    rint as rint,
    round as round,
    row_number as row_number,
    rpad as rpad,
    rtrim as rtrim,
    schema_of_csv as schema_of_csv,
    schema_of_json as schema_of_json,
    sec as sec,
    second as second,
    sentences as sentences,
    sequence as sequence,
    sha1 as sha1,
    sha2 as sha2,
    shiftLeft as shiftLeft,
    shiftRight as shiftRight,
    shiftRightUnsigned as shiftRightUnsigned,
    shiftleft as shiftleft,
    shiftright as shiftright,
    shiftrightunsigned as shiftrightunsigned,
    shuffle as shuffle,
    signum as signum,
    sin as sin,
    sinh as sinh,
    size as size,
    skewness as skewness,
    slice as slice,
    sort_array as sort_array,
    soundex as soundex,
    split as split,
    sqrt as sqrt,
    stack as stack,
    stddev as stddev,
    stddev_pop as stddev_pop,
    stddev_samp as stddev_samp,
    struct as struct,
    substring as substring,
    substring_index as substring_index,
    sum as sum,
    sumDistinct as sumDistinct,
    sum_distinct as sum_distinct,
    tan as tan,
    tanh as tanh,
    timestamp_seconds as timestamp_seconds,
    toDegrees as toDegrees,
    toRadians as toRadians,
    to_binary as to_binary,
    to_csv as to_csv,
    to_date as to_date,
    to_json as to_json,
    to_timestamp as to_timestamp,
    to_utc_timestamp as to_utc_timestamp,
    transform as transform,
    transform_keys as transform_keys,
    transform_values as transform_values,
    translate as translate,
    trim as trim,
    trunc as trunc,
    try_add as try_add,
    try_avg as try_avg,
    try_divide as try_divide,
    try_multiply as try_multiply,
    try_subtract as try_subtract,
    try_sum as try_sum,
    try_to_binary as try_to_binary,
    try_to_number as try_to_number,
    typeof as typeof,
    unbase64 as unbase64,
    unhex as unhex,
    unix_timestamp as unix_timestamp,
    upper as upper,
    var_pop as var_pop,
    var_samp as var_samp,
    variance as variance,
    weekofyear as weekofyear,
    when as when,
    xxhash64 as xxhash64,
    year as year,
    zip_with as zip_with,
)
